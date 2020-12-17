# Needs a refactor

def handle_input(file):
    '''returns input as a list of ints'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = int(lst[i].rstrip('\n'))
    #lst = my_str.split('\n\n')
    return lst

lst = (handle_input('input.txt'))

print(f'My input is {len(lst)} elements long.')

def part_1(lst):
    srtd = sorted(lst)
    #print(srtd)
    ones = 0
    threes = 0
    if srtd[0] == 1:
        ones += 1
    if srtd[0] == 3:
        threes += 1
    for i in range(len(srtd) - 1):
        if srtd[i + 1] - srtd[i] == 1:
            ones += 1
        if srtd[i + 1] - srtd[i] == 3:
            threes += 1
    threes += 1 # to account for build-in joltmeter
    print(f'Part 1: Ones * threes = {ones * threes}')

part_1(lst)

lst = (handle_input('input.txt'))
lst.append(0)
lst = sorted(lst)
#print(lst)

# I'll be honest, I did this by hand, on paper, and it took hours. 
# Keys are the number of integers that are next to each
# other and off by one (as opposed to off by 3), values are the corresponding
# factor. We go through the input list (with 0 appended) and multiply
# these factors together to get the total number of arrangements.
# I can come back and figure out how it works mathematically. 
dct = {3: 2,
       4: 4,
       5: 7,
       6: 13,
       7: 24,
       8: 44}

# How it works:
# All moves boil down to 3 moves. 1-jumpers, which can be done 1 way;
# 2-jumpers, which can be done 2 ways; 3-jumpers, which can be done 4 ways.
# 5-6 --> 1 way
# 5-6-7 --> 2 ways
# 5-6-7-8 --> 4 ways
# Thus, to do 5-6-7-8-9, you may do 5-6 and be left with a 4-jumper (4 ways to do)
# or 5-7 + a 3-jumper (2 ways to do), or 5-8 plus a 1-jumper (1 way to do).
# 4 + 2 + 1 = 7 ways to do a 5-jumper.
#
# Next, to do 5-6-7-8-9-10, you may do 5-6 + 5-jumper, 5-7 + 4-jumper, or
# 5-8 + 3-jumper --> (7 + 4 + 2) = 13 ways to do.
#
# So another approach to this problem would be to go through the list
# and make a list of counts >= 3. Take tha max of this list and
# make a recursion function to populate the dictionary, going as high
# as need be (because my current solution breaks if you string too many
# one-jumpers together.)

prod = 1
count = 1
for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] == 1:
        count += 1
    if lst[i + 1] - lst[i] == 3:
        if count >= 3:
            factor = dct[count]
            prod *= factor
            #print(factor)
        count = 1
if count >= 3:
    factor = dct[count]
    prod *= factor
    #print(factor)
        
print(f'Part 2: {prod} total arrangements')
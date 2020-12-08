# Part 1 tl;dr
#
# Given a list of "boarding passes" of the format 'BFFBFBBLRR'
# where the first 7 characters are B or F and the last 3 characters
# are L or R, and where both sets of characters B/F or L/R can be
# substituted for 1's and 0's to produce binary numbers (this insight
# is not given),
# put all boarding passes through the function (B/F number * 8 + L/R number)
# and find the max.

def handle_input(file):
    '''Accepts source text from problem input webpage 
    (saved as .txt file), returns list of boarding pass strings'''
    inp = open(file)
    my_str = inp.read()
    # for i in range(len(lst)):
    #     lst[i] = lst[i].rstrip('\n')
    lst = my_str.split()
    return lst

boarding_passes = handle_input('input.txt')

# so F = 0, B = 1, then bp[:7] is a binary number
# Then L = 0, R = 1
def find_max_seat_id(boarding_passes):
    highest = 0
    for bp in boarding_passes:
        first = bp[:7]
        last = bp[7:]
        new_first = ''
        new_last = ''
        for _ in first:
            new_first += '0' if _ == 'F' else '1'
        for _ in last:
            new_last += '0' if _ == 'L' else '1'
        seat_id = int(new_first,2) * 8 + int(new_last,2)
        if seat_id > highest:
            highest = seat_id
    return f'{highest} is the highest seat ID.' 

print(find_max_seat_id(boarding_passes))          
            
# Part 2

def find_my_seat_id(boarding_passes):
    lst = []
    for bp in boarding_passes:
        first = bp[:7]
        last = bp[7:]
        new_first = ''
        new_last = ''
        for _ in first:
            new_first += '0' if _ == 'F' else '1'
        for _ in last:
            new_last += '0' if _ == 'L' else '1'
        seat_id = int(new_first,2) * 8 + int(new_last,2)
        lst.append(seat_id)
    lst = sorted(lst)
    for i in range(len(lst) - 1):
        if lst[i+1] - 1 != lst[i]:
            mine = lst[i+1] - 1
    return f'My seat ID is {mine}'
        
print(find_my_seat_id(boarding_passes)) 
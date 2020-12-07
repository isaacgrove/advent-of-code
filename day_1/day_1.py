# Part 1:
# Find the product of the two entries in the input list 
# that sum to 2020 (there are exactly two such entries)
#
# Part 2:
# Same thing, but 3 entries whose sum is 2020

# Uncomment to time functions
#from timeit import default_timer as timer

def find_product1(lst):
    '''Brute-force for Part 1, O(n^2)'''
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == 2020:
                return lst[i] * lst[j]          
    return None
    
def find_product2(lst):
    '''O(n) solution for Part 1. I also tried foregoing the dict 
    and just checking 'if 2020 - ele in lst', but this was slower.'''
    dct = {}
    for i in range(len(lst)):
        dct[lst[i]] = 0
    for ele in lst:
        if 2020 - ele in dct:
            return (2020 - ele) * ele
    return None

def find_triple_product(lst):
    '''O(n^2) solution for Part 2, combines methodologies 
    from the above two functions'''
    dct = {}
    for i in range(len(lst)):
        dct[lst[i]] = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if 2020 - lst[i] - lst[j] in dct:
                return lst[i] * lst[j] * (2020 - lst[i] - lst[j])         
    return None

# Input is a list of ints stored in variable: lst
file = open('input_1.csv')
txt = file.read()
lst = txt.split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

# start = timer()
print(f'Product of the 2 vals that sum to 2020: {find_product2(lst)}')
# end = timer()
# print(f'Timer: {end - start} secs')

# start = timer()
print(f'Product of the 3 vals that sum to 2020: {find_triple_product(lst)}')
# end = timer()
# print(f'Timer: {end - start} secs')
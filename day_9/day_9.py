# tl;dr
# we are to take in a list of integers that is used to "encrypt"
# some data. The list consists of a 25-integer preamble after which
# each integer must be the sum of two of the preceding 25 integers.
# 
# Our first task is to find the first integer that does not follow
# the above rules.
#
# Our second task is to find a continuous set of at least 2 integers
# in the list that sums to the answer of part 1. Then we add the largest
# and smallest integers in this set to get the cypher's "encryption weakness",
# an integer, and our answer.

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

def encryption_breaker(lst):
    preamble = lst[:25]
    # Instead of recalculating all relevant sums each time,
    # let's store them in a dictionary.
    sums = {}
    for i in range(len(preamble)):
        sums[preamble[i]] = set()
        for j in range(i+1,len(preamble)):
            sums[preamble[i]].add(preamble[i] + preamble[j])
    # Check to make sure each new val is a valid sum.
    # If not, we're done. If so, update our sliding preamble and sums.
    for elmt in lst[25:]:
        found = False
        for sum_set in sums.values():
            if elmt in sum_set:
                found = True
                break
        if found:
            # update things
            preamble.append(elmt)
            popped = preamble.pop(0)
            sums.pop(popped)
            sums[elmt] = set()
            for key, value in sums.items():
                value.add(key + elmt) 
        else:
            # we're done
            print(f'First non-sum integer: {elmt}')
            big_num = elmt
            break
    # Part 2: sliding pointers to determine bounds of continguous summation
    # to the answer of Part 1
    left = 0
    right = 1
    summed = lst[left] + lst[right]   
    equal = False
    while not equal:
        if summed < big_num:
            right += 1
            summed += lst[right]
        elif summed > big_num:
            summed -= lst[left]
            left += 1
        else:
            equal = True
    print(f'Encryption weakness: {max(lst[left:right+1]) + min(lst[left:right+1])}')

encryption_breaker(lst)

    
    



    
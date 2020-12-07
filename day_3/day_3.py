# Part 1:
#
# Tl;dr, you are given a large matrix of the format
# [[..#..#..#.],
# [#...#..##..]]   and so on. # = tree, and you need your
# toboggan sled to move down the rows, a specified number
# of steps to the right each time, and you assume that the 
# tree/no tree pattern repeats itself to the right of the
# given matrix.
#
# In Part 1, we find how many trees we would hit on the way down,
# with a slope of "3 steps to the right, 1 step down".
# We always begin in the upper left character, which is always "No Tree"

def handle_input(file):
    '''Accepts source text from personalized problem input webpage,
    returns "tree/no tree" matrix'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst

lst = handle_input('input.txt')
#print(inp)

def tree_counter_pt1(lst):
    rows = len(lst)
    cols = len(lst[0]) #there are cols columns index 0 to (cols - 1)
    trees = 0
    idx = 3
    for row in lst[1:]:
        if row[idx] == '#':
            trees += 1
        if idx <= cols - 4:
            idx += 3
        elif idx == cols - 3:
            idx = 0
        elif idx == cols - 2:
            idx = 1
        elif idx == cols - 1:
            idx = 2
    return trees
        
print(f'Part 1 answer: {tree_counter_pt1(lst)} trees.')
    
# Part 2

#Determine the number of trees you would encounter if, for each 
# of the following slopes, you start at the top-left corner and 
# traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

# What do you get if you multiply together the number of trees 
# encountered on each of the listed slopes?

def tree_counter_pt2(lst):
    rows = len(lst)
    cols = len(lst[0]) #there are cols columns index 0 to (cols - 1)
    factors = []
    
    iters = [1,3,5,7]
    for steps_right in iters:
        trees = 0
        idx = steps_right
        for row in lst[1:]:
            if row[idx] == '#':
                trees += 1
            if idx <= cols - (steps_right + 1):
                idx += steps_right
            else:
                idx = idx + steps_right - cols
        factors.append(trees)
    
    # silly un-Pythonic add-on for final slope
    steps_right = 1
    trees = 0
    idx = steps_right
    for i in range(2,len(lst),2):
        if lst[i][idx] == '#':
            trees += 1
        if idx <= cols - 4:
            idx += steps_right
        else:
            idx = idx + steps_right - cols
    factors.append(trees)
    
    prod = factors[0]
    for factor in factors[1:]:
        prod *= factor

    return prod
        
print(f'Part 2 product: {tree_counter_pt2(lst)}')
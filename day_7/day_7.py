# Our input is a list of rules, one per line,
# where certain bags, identified by color, contain certain numbers 
# of other-colored bags, like Russian nesting dolls, 
# down to the bottom where some colors contain no other bags.
#
# Given that we have a shiny gold bag, we have two tasks:
# Part 1 is to determine how many bags can eventually contain
# the shiny gold.
# Part 2 is to determine how many bags must go inside our (single)
# shiny gold.
#
# The input can be parsed into a graph structure and traversed as such.
# I create two adjacency list representations - for Part 1, dictionary
# keys are bags, and values are "bags in which this bag can exist".
# For Part 2, keys are bags and values are themselves dictionaries - 
# keys being bags that go inside, values being the number of
# such bags.
#
# Example rules: 
# 1) vibrant lime bags contain 3 faded gold bags, 
#    3 plaid aqua bags, 2 clear black bags.
# 2) clear black bags contain no other bags.

import re

def handle_input(file):
    '''Accepts source text from problem input webpage 
    (saved as .txt file), returns list of groups'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    #lst = my_str.split('\n\n')
    return lst

lst = (handle_input('input.txt'))
print(f'There are {len(lst)} rules in the input (including for reference).')

def parse_input_pt1(lst, dct={}):
    '''creates a dict where the key can go directly inside all values'''
    num_color_regex = re.compile(r'[0-9]+\s\w+\s\w+')
    for string in lst:
        # split string into bag in question, bags it can contain
        subs = string.split(' bags contain ')
        # list of bags it can contain
        mo = num_color_regex.findall(subs[1])
        for entry in mo:
            if entry[2:] not in dct:
                dct[entry[2:]] = {subs[0]}
            else:
                dct[entry[2:]].add(subs[0])          
    return dct

dct = parse_input_pt1(lst)

# let's DFS search the dct starting at shiny gold
# not worried about complexity; visits the visited
res = set()
stack = ['shiny gold']
while stack:
    node = stack.pop()
    res.add(node)
    for neighbor in dct[node]:
        if neighbor not in dct:
            res.add(neighbor)
            continue
        stack.append(neighbor)
res.remove('shiny gold')
print(f'Part 1: there are {len(res)} bags that can contain shiny gold bags.')


# Part 2

# re-builds dct with contains: contained relationships
def build_dct_contains(lst, dct={}):
    num_color_regex = re.compile(r'[0-9]+\s\w+\s\w+')
    for string in lst:
        # split string into bag in question, bags it can contain
        subs = string.split(' bags contain ')
        # list of bags it can contain
        mo = num_color_regex.findall(subs[1])
        # don't care about how many will fit
        lil_dct = {}
        for entry in mo:
            lil_dct[entry[2:]] = int(entry[0])
        dct[subs[0]] = lil_dct
    return dct

dct = build_dct_contains(lst)

def recurse(root, total, prod=1, num=1):
    # base case - no children
    if len(dct[root]) == 0:
        total.append(prod)
        return
    # otherwise, has children we need to recurse.
    # prod carries through
    for neighbor, value in dct[root].items():
        recurse(neighbor, total, prod*value, value)
    total.append(prod)
            
def bag_counter(root):
    tot = []
    recurse('shiny gold', tot, prod=1, num=1)
    
    return sum(tot) - 1

result = bag_counter('shiny gold')
print(f'Part 2: My shiny gold bag requires {result} bags inside it.')
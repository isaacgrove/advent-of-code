def handle_input(file):
    '''Accepts source text from problem input webpage 
    (saved as .txt file), returns list of groups'''
    inp = open(file)
    my_str = inp.read()
    # for i in range(len(lst)):
    #     lst[i] = lst[i].rstrip('\n')
    lst = my_str.split('\n\n')
    return lst

groups = handle_input('input.txt')
print(f'There are {len(groups)} total groups')

def sum_anyone_yeses(groups):
    for i in range(len(groups)):
        groups[i] = groups[i].replace('\n', '')
    tot = 0
    for group in groups:
        visited = set()
        for char in group:
            if char not in visited:
                visited.add(char)
        tot += len(visited)
    return f'The answer to Part 1 is {tot}'

print(sum_anyone_yeses(groups))

# Part 2
#
# oops we actually need the questions to which EVERYONE in a 
# group answered yes
groups = handle_input('input.txt')

def sum_everyone_yeses(groups):
    # instead of removing newlines, split passengers by newline
    for i in range(len(groups)):
        groups[i] = groups[i].split('\n')
    tot = 0
    for group in groups:
        a = set(group[0])
        for person in group:
            a = a.intersection(set(person))
        #print(tot)
        tot += len(a)
    #hackily adding the last group on
    a = set(groups[-1][0])
    for person in groups[-1][:-1]:
        a = a.intersection(set(person))
    tot += len(a)
    return f'The answer to Part 2 is {tot}'

print(sum_everyone_yeses(groups))
# attempt 1 - 3431 is too low
# attempt 2 - 3435 is correct. There was a \n at the enc of the input
# causing the final set intersection to be zero rather than the number
# of "everyone said yes"'s.
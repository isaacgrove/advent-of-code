def handle_input(file):
    '''returns input as a list of ints'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = int(lst[i].rstrip('\n'))
    #lst = my_str.split('\n\n')
    return lst

lst = (handle_input('input.txt'))
lst.append(0)
lst = sorted(lst)
print(lst)

print(f'My input is {len(lst)} elements long.')
dct = {3: 2,
       4: 4,
       5: 7,
       6: 13,
       7: 24,
       8: 44}

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
        
print(f'{prod} total arrangements')
            
    
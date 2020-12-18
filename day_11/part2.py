def handle_input(file):
    '''returns input as a list of ints'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
        new_lst = []
        for char in lst[i]:
            if char == 'L':
                new_lst.append(1)
            else:
                new_lst.append(0)
        lst[i] = new_lst
    
    return lst
lst = (handle_input('input.txt'))
print(f'Seating area is {len(lst)} rows deep by {len(lst[0])} seats wide.')

# Can use for testing. The layouts after each iteration are given, as is the fact
# that 26 seats should be occupied at the end
#
# lst = [[1,0,1,1,0,1,1,0,1,1],
#        [1,1,1,1,1,1,1,0,1,1],
#        [1,0,1,0,1,0,0,1,0,0],
#        [1,1,1,1,0,1,1,0,1,1],
#        [1,0,1,1,0,1,1,0,1,1],
#        [1,0,1,1,1,1,1,0,1,1],
#        [0,0,1,0,1,0,0,0,0,0],
#        [1,1,1,1,1,1,1,1,1,1],
#        [1,0,1,1,1,1,1,1,0,1],
#        [1,0,1,1,1,1,1,0,1,1]
#        ]

def look_left(i,j,lst):
    # all 8 of these return a 1 if you see an occupied seat, a 0 if you see an unoccupied seat
    if j - 1 >= 0:
        if lst[i][j-1] == 2:
            return 1
        elif lst[i][j-1] == 1:
            return 0
        else:
            return look_left(i, j-1, lst)
    else:
        return 0
    
def look_right(i,j,lst):
    if j + 1 <= (len(lst) - 1):
        if lst[i][j+1] == 2:
            return 1
        elif lst[i][j+1] == 1:
            return 0
        else:
            return look_right(i, j+1, lst)
    else:
        return 0

def look_up(i,j,lst):
    if i - 1 >= 0:
        if lst[i-1][j] == 2:
            return 1
        elif lst[i-1][j] == 1:
            return 0
        else:
            return look_up(i-1, j, lst)
    else:
        return 0

def look_down(i,j,lst):
    if i + 1 <= (len(lst) - 1):
        if lst[i+1][j] == 2:
            return 1
        elif lst[i+1][j] == 1:
            return 0
        else:
            return look_down(i+1, j, lst)
    else:
        return 0

def look_up_left(i,j,lst):
    if i - 1 >= 0 and j - 1 >= 0:
        if lst[i-1][j-1] == 2:
            return 1
        elif lst[i-1][j-1] == 1:
            return 0
        else:
            return look_up_left(i-1, j-1, lst)
    else:
        return 0

def look_down_left(i,j,lst):
    if j - 1 >= 0 and i + 1 <= (len(lst) - 1):
        if lst[i+1][j-1] == 2:
            return 1
        elif lst[i+1][j-1] == 1:
            return 0
        else:
            return look_down_left(i+1, j-1, lst)
    else:
        return 0

def look_down_right(i,j,lst):
    if i+1 <= (len(lst) - 1) and j + 1 <= (len(lst) - 1):
        if lst[i+1][j+1] == 2:
            return 1
        elif lst[i+1][j+1] == 1:
            return 0
        else:
            return look_down_right(i+1, j+1, lst)
    else:
        return 0

def look_up_right(i,j,lst):
    if i - 1 >= 0 and j + 1 <= (len(lst) - 1):
        if lst[i-1][j+1] == 2:
            return 1
        elif lst[i-1][j+1] == 1:
            return 0
        else:
            return look_up_right(i-1, j+1, lst)
    else:
        return 0
    
def look_8_ways(i,j,lst):
    adj_occ = 0
    adj_occ += look_left(i,j,lst)
    adj_occ += look_right(i,j,lst)
    adj_occ += look_up(i,j,lst)
    adj_occ += look_down(i,j,lst)
    adj_occ += look_up_left(i,j,lst)
    adj_occ += look_up_right(i,j,lst)
    adj_occ += look_down_left(i,j,lst)
    adj_occ += look_down_right(i,j,lst)
    return adj_occ


# You have to copy each inner list, or else those are just
# passed by reference and copying the outer list effectively does nothing
refresh = [row.copy() for row in lst]

changed = True
iters = 0
while changed:
    changed = False
    # make lst the old refresh
    lst = [row.copy() for row in refresh]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                if look_8_ways(i,j,lst) == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                if look_8_ways(i,j,lst) >= 5:
                    refresh[i][j] = 1
                    changed = True
    iters += 1
    print(iters)

print(f'{iters} iterations.')

occupied = 0
for i in range(len(refresh)):
    for j in range(len(refresh[i])):
        if refresh[i][j] == 2:
            occupied += 1
print(f'{occupied} occupied seats.')
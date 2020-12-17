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

# You have to copy each inner list, or else those are just
# passed by reference and copying the outer list effectively does nothing
refresh = [row.copy() for row in lst]

changed = True
iters = 0
while changed:
    changed = False
    # make lst the old refresh
    lst = [row.copy() for row in refresh]
    for i in range(1,96):
        for j in range(1,96):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                for seat in lst[i -1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                for seat in lst[i -1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        for j in range(0,1):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                for seat in lst[i+1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                for seat in lst[i+1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        
      ## HERE PROBABLY ##
        
        for j in range(96,97):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                for seat in lst[i+1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                for seat in lst[i+1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
    for i in range(0,1):
        # 3 cases. j = 0, j = 1-95, j = 96
        for j in range(0,1):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        for j in range(1,96):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        for j in range(96,97):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i+1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
    for i in range(96,97):
        # 3 cases. j = 0, j = 1-95, j = 96
        for j in range(0,1):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        for j in range(1,96):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                if lst[i][j+1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+2]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
                    refresh[i][j] = 1
                    changed = True
        for j in range(96,97):
            if lst[i][j] == 1:
                # seat is unoccupied. Check adjacent 8 seats.
                # If all are empty, seat becomes occupied.
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ == 0:
                    refresh[i][j] = 2
                    changed = True
            if lst[i][j] == 2:
                # seat is occupied. Count adjacent 8 seats.
                # If 4 or more are occupied, seat becomes empty
                adj_occ = 0
                if lst[i][j-1] == 2:
                    adj_occ += 1
                for seat in lst[i-1][j-1:j+1]:
                    if seat == 2:
                        adj_occ += 1
                if adj_occ >= 4:
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
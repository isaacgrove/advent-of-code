# attempt at a faster version of Part 1. Not working, needs debugged.


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

lst = [[1,0,1,1,0,1,1,0,1,1],
       [1,1,1,1,1,1,1,0,1,1],
       [1,0,1,0,1,0,0,1,0,0],
       [1,1,1,1,0,1,1,0,1,1],
       [1,0,1,1,0,1,1,0,1,1],
       [1,0,1,1,1,1,1,0,1,1],
       [0,0,1,0,1,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1],
       [1,0,1,1,1,1,1,1,0,1],
       [1,0,1,1,1,1,1,0,1,1]
       ]

# You have to copy each inner list, or else those are just
# passed by reference and copying the outer list effectively does nothing

changed = True
iters = 0
while changed:
    changed = False
    new_lst = []
    for i in range(len(lst)):
        new_row = []
        for j in range(len(lst[i])):
            # first row
            if i == 0:
                # first column
                if j == 0:
                    # 0,0
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                # last column
                elif j == (len(lst) - 1):
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                    # 0,end
                # middle columns
                else:
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
            # last row
            elif i == len(lst) - 1:
                # first column
                if j == 0:
                    # end,0
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                # last column
                elif j == len(lst) - 1:
                    # end,end
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                # middle columns
                else:
                    # end,middle
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
            # middle rows
            else:
                # first column
                if j == 0:
                    # middle,0
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                # last column
                elif j == len(lst) - 1:
                    # middle,end
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
                # middle columns
                else:
                    # middle,middle
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
                            new_row.append(2)
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
                            new_row.append(1)
                            changed = True
        new_lst.append(new_row)
    lst = new_lst
    iters += 1
    print(iters)

print(f'{iters} iterations.')

occupied = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            occupied += 1
print(f'{occupied} occupied seats.')
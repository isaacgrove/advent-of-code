# The instructions in input.txt mean the following:
#
# Part 1:
# NSEW (compass directions) move the ship X units in that direction.
# RL are rotations - which way the ship faces.
# F means "move forward" - in the direction of its heading.
# We are to find the "Manhattan distance" of the ship (the sum of
# the ship's N/S and E/W deviations from its original location, respectively)
#
# Part 2:
# It is "discovered" that you were using the wrong interpretation of the instructions.
# Now, NSEWRL all refer to a waypoint, and F is the only instruction that moves the ship.
# NSEW moves the waypoint X units in that direction.
# RL rotates the waypoint X number of degrees about the ship, either right or left.
# The waypoint is always relative to the ship, so if it is at N20, W15, then it is still
# N20, W15 even if the ship moves.
# Again, find the Manhattan distance from the ship's original location.


def handle_input(file):
    '''returns input as a list of ints'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst
lst = (handle_input('input.txt'))
print(f'Input is {len(lst)} instructions long.')

def part1():
    ew_coord = 0 # west is pos
    ns_coord = 0 # north is pos
    heading = 90
    compass = {90: 'east',
            180: 'south',
            270: 'west',
            0: 'north'}
    for inst in lst:
        act = inst[0]
        val = int(inst[1:])
        if act == 'W':
            ew_coord += val
        elif act == 'E':
            ew_coord -= val
        elif act == 'N':
            ns_coord += val
        elif act == 'S':
            ns_coord -= val
        elif act == 'F':
            if compass[heading] == 'east':
                ew_coord -= val
            if compass[heading] == 'west':
                ew_coord += val
            if compass[heading] == 'north':
                ns_coord += val
            if compass[heading] == 'south':
                ns_coord -= val
        elif act == 'R':
            heading += val
            heading = heading % 360
        else:
            # act == 'L':
            heading -= val
            while heading < 0:
                heading += 360
            heading = heading % 360
    print(f'Manhattan distance for Part 1: {abs(ns_coord) + abs(ew_coord)}')
    
part1()

def part2():
    ew_ship = 0 # east is pos
    ns_ship = 0 # north is pos
    ew_waypoint = 10 # waypoint starts 10 units east and 1 unit north (of ship)
    ns_waypoint = 1
    for inst in lst:
        act = inst[0]
        val = int(inst[1:])
        if act == 'W':
            ew_waypoint -= val
        elif act == 'E':
            ew_waypoint += val
        elif act == 'N':
            ns_waypoint += val
        elif act == 'S':
            ns_waypoint -= val
        elif act == 'R':
            if val == 90:
                if (ew_waypoint > 0 and ns_waypoint > 0) or (ew_waypoint < 0 and ns_waypoint < 0): # northeast or southwest, R90
                    # flip values, ew maintains sign, ns flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign
                    ns_waypoint = abs(holder) * ns_sign * -1
                elif (ew_waypoint < 0 and ns_waypoint > 0) or (ew_waypoint > 0 and ns_waypoint < 0): # northwest or southeast, R90
                    # flip values, ns maintains sign, ew flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign * -1
                    ns_waypoint = abs(holder) * ns_sign
                else: # waypoint lies on a cardinal direction
                    if ns_waypoint != 0:
                        ew_waypoint = ns_waypoint
                        ns_waypoint = 0
                    elif ew_waypoint != 0:
                        ns_waypoint = ew_waypoint * -1
                        ew_waypoint = 0
            elif val == 180:
                ew_waypoint *= -1
                ns_waypoint *= -1
            elif val == 270:
                if (ew_waypoint > 0 and ns_waypoint > 0) or (ew_waypoint < 0 and ns_waypoint < 0): # northeast or southwest, R270
                    # flip values, ns maintains sign, ew flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign * -1
                    ns_waypoint = abs(holder) * ns_sign
                elif (ew_waypoint < 0 and ns_waypoint > 0) or (ew_waypoint > 0 and ns_waypoint < 0): # northwest or southeast, R270
                    # flip values, ew maintains sign, ns flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign
                    ns_waypoint = abs(holder) * ns_sign * -1
                else: # waypoint lies on a cardinal direction
                    if ns_waypoint != 0:
                        ew_waypoint = ns_waypoint * -1
                        ns_waypoint = 0
                    elif ew_waypoint != 0:
                        ns_waypoint = ew_waypoint
                        ew_waypoint = 0
            else:
                count += 1
        elif act == 'L':
            if val == 90:
                if (ew_waypoint > 0 and ns_waypoint > 0) or (ew_waypoint < 0 and ns_waypoint < 0): # northeast or southwest, R270
                    # flip values, ns maintains sign, ew flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign * -1
                    ns_waypoint = abs(holder) * ns_sign
                elif (ew_waypoint < 0 and ns_waypoint > 0) or (ew_waypoint > 0 and ns_waypoint < 0): # northwest or southeast, R270
                    # flip values, ew maintains sign, ns flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign
                    ns_waypoint = abs(holder) * ns_sign * -1
                else: # waypoint lies on a cardinal direction
                    if ns_waypoint != 0:
                        ew_waypoint = ns_waypoint * -1
                        ns_waypoint = 0
                    elif ew_waypoint != 0:
                        ns_waypoint = ew_waypoint
                        ew_waypoint = 0
            elif val == 180:
                ew_waypoint *= -1
                ns_waypoint *= -1
            elif val == 270:
                if (ew_waypoint > 0 and ns_waypoint > 0) or (ew_waypoint < 0 and ns_waypoint < 0): # northeast or southwest, R90
                    # flip values, ew maintains sign, ns flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign
                    ns_waypoint = abs(holder) * ns_sign * -1
                elif (ew_waypoint < 0 and ns_waypoint > 0) or (ew_waypoint > 0 and ns_waypoint < 0): # northwest or southeast, R90
                    # flip values, ns maintains sign, ew flips sign
                    ew_sign = ew_waypoint / abs(ew_waypoint)
                    ns_sign = ns_waypoint / abs(ns_waypoint)
                    holder = ew_waypoint
                    ew_waypoint = abs(ns_waypoint) * ew_sign * -1
                    ns_waypoint = abs(holder) * ns_sign
                else: # waypoint lies on a cardinal direction
                    if ns_waypoint != 0:
                        ew_waypoint = ns_waypoint
                        ns_waypoint = 0
                    elif ew_waypoint != 0:
                        ns_waypoint = ew_waypoint * -1
                        ew_waypoint = 0
        else:
            #act == 'F'
            ns_ship += (ns_waypoint * val)
            ew_ship += (ew_waypoint * val)
        # print('wp ', ew_waypoint, ns_waypoint)
        # print('sh ', ew_ship, ns_ship, '\n--------------')
    print(f'Manhatten distance for Part 2: {int(abs(ns_ship) + abs(ew_ship))}')
    
part2()
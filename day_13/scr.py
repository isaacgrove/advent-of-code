def handle_input(file):
    '''returns two lines of output, my arrival time at airport and bus ID's
    with x's assumed to be out-of-service buses'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst
lst = (handle_input('input.txt'))

# def part1():
#     arrival = int(lst[0])
#     print('I can be at the airport at timestamp ', arrival)
#     buses = []
#     for bus in lst[1].split(','):
#         if bus != 'x':
#             buses.append(int(bus))
#     print('Bus IDs                 ', buses)

#     next_in = []
#     for bus in buses:
#         mults = arrival // bus
#         next_in.append(bus*(mults + 1) - arrival)
#     print('Next bus in (by index)  ', next_in)

#     a = buses[next_in.index(min(next_in))]
#     b = min(next_in)
#     print(f'The very next bus is Bus {a} in {b} minutes \nPart 1 answer is the product: {a*b}' )
# #part1()




# Part 2

buses = lst[1].split(',')
print(buses)

# buses = [29, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', '37', 
#          'x', 'x', 'x', 'x', 'x', 467, 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 23, 'x', 'x', 
#          'x', 'x', 13, 'x', 'x', 'x', 17, 'x', 
#          19, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 443, 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 
#          'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 41]
# example sets
#
# buses = [7,13,'x','x',59,'x',31,19] # 7 at 0, answer 1068781
# buses = [17,'x',13,19] # 17 at 0, answer 3417
# buses = [1789,37,47,1889] # 1789 at 0, answer 1202161486
# buses = [67,7,'x',59,61]  # 67 at key 0, answer 1261476
# buses = [67,'x',7,59,61]  # 67 at key 0, answer 779210
num = []
idx = []
rem = []
pp = []
for bus in buses:
    if bus != 'x':
        num.append(int(bus))
        idx.append(buses.index(bus))
print('num', num)
print('idx', idx)

for i in range(len(num)):
    rem.append(abs(idx[i] - num[i]))
    rem[0] = 0
print('rem', rem)

prod = 1
for bus in num:
    prod *= bus
print('prod', prod)

for bus in num:
    pp.append(int(prod/bus))
print('pp', pp)

# inv[i] = Modular Multiplicative Inverse of 
#          pp[i] with respect to num[i]
inv = []
def modInverse(a, m): 
    '''a = pp[i], m = num[i]'''
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1
# print(modInverse(20,3))
# print(modInverse(15,4))
# print(modInverse(12,5))

for i in range(len(num)):
    inv.append(modInverse(pp[i],num[i]))
print('inv', inv)

big = 0
for i in range(len(num)):
    big += (rem[i]*pp[i]*inv[i])
print('big', big)
print(big % prod)


# This and related articles (Set 1, Set 2, Modular Multiplicative Inverse)
# https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/?ref=rp



# Guess 188,854,586,424,117 is too low
# Guess 848,881,884,520,803 is too high ???????????



# I just couldn't get this to work - stalls out in the 100's of trillions
#
# largest = max(bus_dict.keys())
# largest_idx = bus_dict[max(bus_dict.keys())]
# time = 29
# found = False
# while not found:
#     found = True
#     print(time)
#     mults = time // largest
#     next_bus = largest * (mults + 1)
#     if next_bus % time == largest_idx:
#         print('Key!', largest, 'Time: ', time)
#         break
#     if next_bus % time != largest_idx:
#         found = False
#     time += 29
# # Key 467, Time 13514
# bus_dict.pop(467)
# largest = 37
# largest_idx = 23
# found = False
# while not found:
#     found = True
#     print(time)
#     mults = time // largest
#     next_bus = largest * (mults + 1)
#     if next_bus % time == largest_idx:
#         print('Key!', largest, 'Time: ', time)
#         break
#     if next_bus % time != largest_idx:
#         found = False
#     time += (29*467)
# print(time)
# # Key 37, time 81229

# bus_dict.pop(37)
# largest = 443
# largest_idx = 60
# found = False
# while not found:
#     found = True
#     print(time)
#     mults = time // largest
#     next_bus = largest * (mults + 1)
#     if next_bus % time == largest_idx:
#         print('Key!', largest, 'Time: ', time)
#         break
#     if next_bus % time != largest_idx:
#         found = False
#     time += (29*467*37)
# print(time)
# # Key 443, time 158927076

# bus_dict.pop(443)
# largest = 41
# largest_idx = 101
# found = False
# while not found:
#     found = True
#     print(time)
#     mults = time // largest
#     next_bus = largest * (mults + 1)
#     if next_bus % time == largest_idx:
#         print('Key!', largest, 'Time: ', time)
#         break
#     if next_bus % time != largest_idx:
#         found = False
#     time += (29*467*37*443)

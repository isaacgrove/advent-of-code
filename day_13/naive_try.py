# Here's are a couple of wild and crazy attempts
# at doing the naive approach
#
# I just couldn't get this to work - stalls out 
# in the 100's of trillions
# A further attempt leads me to believe I have something slightly wrong.
# And that this should still work. I ran one trial 
# up to 1.4 quadrillion and the answer is only 690 trillion
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
bus_dict = {} # stores bus as key, index as value
for bus in buses:
    if bus != 'x':
        bus_dict[int(bus)] = buses.index(bus)
bus_dict.pop(29)
print(bus_dict)


# example sets
#
#bus_dict = {13: 2,
#            19: 3} # 17 at 0, answer 3417
# bus_dict = {37: 1,
#             47: 2,
#             1889: 3} # 1789 at 0, answer 1202161486 
# bus_dict = {7: 1,
#             59: 2,
#             61: 3}


largest = max(bus_dict.keys())
largest_idx = bus_dict[max(bus_dict.keys())]
time = 29
found = False
while not found:
    found = True
    print(time)
    mults = time // largest
    next_bus = largest * (mults + 1)
    if next_bus % time == largest_idx:
        print('Key!', largest, 'Time: ', time)
        break
    if next_bus % time != largest_idx:
        found = False
    time += 29
# Key 1889, Time 2467031
#time += (1889*1789)
bus_dict.pop(467)
largest = 443
largest_idx = 60
found = False
while not found:
    found = True
    print(time)
    mults = time // largest
    next_bus = largest * (mults + 1)
    if next_bus % time == largest_idx:
        print('Key!', largest, 'Time: ', time)
        break
    if next_bus % time != largest_idx:
        found = False
    time += (29*467)
print(time)
# Key 47, time 90331977
bus_dict.pop(443)
largest = 37
largest_idx = 23
found = False
while not found:
    found = True
    print(time)
    mults = time // largest
    next_bus = largest * (mults + 1)
    if next_bus % time == largest_idx:
        print('Key!', largest, 'Time: ', time)
        break
    if next_bus % time != largest_idx:
        found = False
    time += (29*467*443)
# Key 37, time 1202161486
bus_dict.pop(37)
largest = 23
largest_idx = 37
found = False
# manual time resets
#time = 258614492288397
# time = 455145420603130
#time = 681901818799256
#time = 719411893080057
time = 1936353494760060 # 1.9 quadrillion
while not found:
    found = True
    print(time)
    mults = time // largest
    next_bus = largest * (mults + 1)
    if next_bus % time == largest_idx:
        print('Key!', largest, 'Time: ', time)
        break
    if next_bus % time != largest_idx:
        found = False
    time += (29*467*443*37)


print(bus_dict)
# ========= # ========= # ========= # =========

# time = 2010
# found = False
# while not found:
#     print(time)
#     found = True
#     for key, val in bus_dict.items():
#         mults = time // key
#         next_bus = key * (mults + 1)
#         if next_bus % time == val:
#             print('Key!', key, 'Time: ', time)
#         if next_bus % time != val:
#             found = False
#     time += (61*67) # fill in the bus at index 0


# This solution works but is hopelessly slow.
# Need to get to 100 trillion, takes a minute to get to 100 million
# time = 17 # fill in the bus at index 0
# found = False
# while not found:
#     found = True
#     for key, val in bus_dict.items():
#         # print(key)
#         # print(time)
#         mults = time // key
#         #print(mults)
#         next_bus = key * (mults + 1)
#         # print(next_bus)
#         # print((next_bus - val) % time)
#         if next_bus % time != val:
#             found = False
#     print(time)
#     time += 17 # fill in the bus at index 0


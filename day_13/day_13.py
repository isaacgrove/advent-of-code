# Part 2 uses Chinese remainder theorem to work with large
# numbers.

# This and related G4G articles (Set 1, Set 2, Modular Multiplicative Inverse)
# https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/?ref=rp

def handle_input(file):
    '''returns two lines of output, my arrival time at airport and bus ID's
    with x's assumed to be out-of-service buses'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst
lst = (handle_input('input.txt'))

def part1():
    arrival = int(lst[0])
    print('I can be at the airport at timestamp ', arrival)
    buses = []
    for bus in lst[1].split(','):
        if bus != 'x':
            buses.append(int(bus))
    print('Bus IDs                 ', buses)

    next_in = []
    for bus in buses:
        mults = arrival // bus
        next_in.append(bus*(mults + 1) - arrival)
    print('Next bus in (by index)  ', next_in)

    a = buses[next_in.index(min(next_in))]
    b = min(next_in)
    print(f'The very next bus is Bus {a} in {b} minutes \nPart 1 answer is the product: {a*b}' )
part1()




# Part 2
def part2():
    buses = lst[1].split(',')

    # Test cases
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
    # print('num', num)
    # print('idx', idx)

    for i in range(len(num)):
        # index cannot exceed the bus ID. This caused me to
        # pass all 6 test cases on the problem without finding
        # the answer for a long time.
        idx_clone = idx[i]
        num_clone = num[i]
        while idx_clone >= num_clone:
            num_clone += num[i]
        rem.append(abs(idx_clone - num_clone))
        rem[0] = 0
    #print('rem', rem)

    prod = 1
    for bus in num:
        prod *= bus
    #print('prod', prod)

    for bus in num:
        pp.append(int(prod/bus))
    #print('pp', pp)

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
    #print('inv', inv)

    big = 0
    for i in range(len(num)):
        big += (rem[i]*pp[i]*inv[i])
    #print('big', big)
    print('Part 2: the first time the buses line up, t =', big % prod)

part2()

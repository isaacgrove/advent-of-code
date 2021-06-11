def handle_input(file):
    '''returns two lines of output, my arrival time at airport and bus ID's
    with x's assumed to be out-of-service buses'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst
lst = (handle_input('input.txt'))
print('list length', len(lst))

mask = '0'*36
#print(mask)
mem = {}
#count = 0
#print(lst[68:71])
for inst in lst:
    #count += 1
    #print(count)
    if inst[:4] == 'mask': # update mask    good
        mask = inst[7:]
    else: # update value at memory address
        address = int(inst.split()[0].lstrip('mem[').rstrip(']'))
        val = int(inst.split()[-1])
        #print(bin(val))
        val_str = str(bin(val)).lstrip('0b')
        while len(val_str) < 36:
            val_str = '0' + val_str
        # print(val_str)
        # print(mask)
        # print(len(val_str))
        # print(len(mask))
        new_str = ''
        for i in range(36):
            if mask[i] == val_str[i] or mask[i] == 'X':
                new_str += val_str[i]
            else:
                new_str += mask[i]
        #print(new_str)
        #print(int(new_str,2))
        mem[address] = int(new_str,2)
print(len(mem.keys()))
print(sum(mem.values()))
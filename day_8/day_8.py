# We are given input instructions like so:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
#
# and so on. My instructions are 638 long.
# 'nop' means do nothing and move to the next instruction.
# 'acc' means add the integer to an accumulator variable.
# 'jmp' means move to another instruction, integer spaces away (up or down).
# 
# The instructions inherently have an infinite loop.
#
# We have two tasks:
#
# 1) Find what the accumulator is immediately before repeating
# any instruction
#
# 2) Within the instructions, there is one 'jmp' or 'nop' instruction
# which can be replaced with the other to allow termination of the full
# list of instructions (which occurs when the program tries to execute an
# instruction immediately after the final one in the list).
# Fix the incorrect instruction and return the accumulator at the end
# of the program


def handle_input(file):
    '''Accepts source text from problem input webpage 
    (saved as .txt file), returns list of boot code instructions'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    #lst = my_str.split('\n\n')
    return lst

lst = (handle_input('input.txt'))
print(f'There are {len(lst)} instructions in the input (including for reference).')


# Part 1

def pt1_accumulator_before_loop():
    accumulator = 0

    visited = [False]*len(lst)
    idx = 0
    while visited[idx] == False:
        visited[idx] = True
        if lst[idx][:3] == 'acc':
            accumulator += int(lst[idx][4:])
            idx += 1
        elif lst[idx][:3] == 'jmp':
            idx += int(lst[idx][4:])
        else:
            idx += 1
    print(f'Part 1: the accumulator is {accumulator} before the loop.')

pt1_accumulator_before_loop()

# Part 2

def run_boot_code(lst, end_found):
    visited = [False]*len(lst)
    accumulator = 0
    idx = 0
    while visited[idx] == False:
        visited[idx] = True
        if lst[idx][:3] == 'acc':
            accumulator += int(lst[idx][4:])
            idx += 1
        elif lst[idx][:3] == 'jmp':
            idx += int(lst[idx][4:])
        else:
            idx += 1
        if idx == len(lst):
            print('Part 2: accumulator = ', accumulator, 'upon boot code termination.')
            end_found.append('hi')
            break

def pt2_accumulator_after_termination():
    idx_replaced = 0
    end_found = []
    acc = 0
    while len(end_found) == 0:
        lst2 = lst.copy()
        for i in range(idx_replaced + 1, len(lst)):
            if lst2[i][:3] == 'jmp':
                lst2[i] = lst2[i].replace('jmp', 'nop')
                idx_replaced = i
                break
            if lst2[i][:3] == 'nop':
                lst2[i] = lst2[i].replace('nop', 'jmp')
                idx_replaced = i
                break
        run_boot_code(lst2, end_found)
        acc += 1

pt2_accumulator_after_termination()
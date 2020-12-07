# Problem 2, Part 1
#
# To try to debug the problem, they have created a list (your puzzle input) 
# of passwords (according to the corrupted database) and the corporate 
# policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times 
# a given letter must appear for the password to be valid. For example, 
# 1-3 a means that the password must contain a at least 1 time and 
# at most 3 times.

# In the above example, 2 passwords are valid. 
# The middle password, cdefg, is not; it contains no instances of b, 
# but needs at least 1. The first and third passwords are valid: they contain 
# one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?

def handle_input(file):
    '''Accepts source text from personalized problem input webpage,
    returns list of password policies and passwords'''
    inp = open(file)
    lst = inp.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip('\n')
    return lst

def valid_password_counter(lst):
    '''Solution for Part 1. Counts instances of the 
    policy_char in each password, determines if the password
    is valid within the bounds of its given policy, 
    and returns the total number of valid passwords.'''
    valid_passwords = 0
    for policy in lst:
        policy_char = policy.split()[1].rstrip(':')
        password = policy.split()[2]
        lb = int(policy.split()[0].split('-')[0])
        ub = int(policy.split()[0].split('-')[1])
        char_count = 0
        for char in password:
            if char == policy_char:
                char_count += 1
        if char_count >= lb and char_count <= ub:
            valid_passwords += 1
    return valid_passwords

lst = handle_input('input.csv')

print(f'Part 1 answer: {valid_password_counter(lst)} valid passwords.')

# Part 2

# The shopkeeper suddenly realizes that he just accidentally explained 
# the password policy rules from his old job at the sled rental place 
# down the street! The Official Toboggan Corporate Policy actually works 
# a little differently.

# Each policy actually describes two positions in the password, 
# where 1 means the first character, 2 means the second character, 
# and so on. (Be careful; Toboggan Corporate Policies have no concept 
# of "index zero"!) Exactly one of these positions must contain the 
# given letter. Other occurrences of the letter are irrelevant for the 
# purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to 
# the new interpretation of the policies?



# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
#
# Methodology
# The character we need to count is str.split()[1]
# lower bound = password.split()[0]
# 

def valid_password_counter_policy2(lst):
    '''Solution for Part 2. No longer counting instances of char.
    Instead, checking if index 1 or index 2, but not both,
    contain our policy_char'''
    valid_passwords = 0
    for policy in lst:
        policy_char = policy.split()[1].rstrip(':')
        password = policy.split()[2]
        idx1 = int(policy.split()[0].split('-')[0]) - 1
        idx2 = int(policy.split()[0].split('-')[1]) - 1
        truths = 0
        if password[idx1] == policy_char:
            truths += 1
        if password[idx2] == policy_char:
            truths += 1
        if truths == 1:
            valid_passwords += 1
    return valid_passwords

print(f'Part 2 answer: {valid_password_counter_policy2(lst)} valid passwords.')
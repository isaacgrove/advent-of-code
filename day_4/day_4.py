# Part 1 tl;dr

# "Passports" are supposed to contain the following fields:
#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# Out of a batch of passports, determine how many are valid.
# 'cid' is optional (since, in the fun word problem, our passport
# doesn't have this field and we need to get around the requirement)

def handle_input(file):
    '''Accepts source text from problem input webpage 
    (saved as .txt file), returns list of passports'''
    inp = open(file)
    my_str = inp.read()
    # for i in range(len(lst)):
    #     lst[i] = lst[i].rstrip('\n')
    lst = my_str.split('\n\n')
    print(f'There are {len(lst)} total passports.')
    return lst

passports = handle_input('input.txt')

def passport_checker_pt1(passports):
    reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for passport in passports:
        val = True
        for req in reqs:
            if req not in passport:
                val = False
        if val:
            valid += 1
    return valid

print(f'There are {passport_checker_pt1(passports)} valid passports in Part 1.')

# Part 2
import re

def passport_checker_pt2(passports):
    '''We now have strict requirements for each field of the passport.
    We check each requirement with a regex. Any failure constitutes an
    invalid passport. Return total number of valid passports.'''
    valid = 0
    for passport in passports:
        val = True
        # byr - four digits; at least 1920 and at most 2002.
        byr = re.compile(r'byr:\d\d\d\d')
        mo = byr.search(passport)
        if not mo:
            val = False
        else:
            if int(mo.group()[4:]) < 1920 or int(mo.group()[4:]) > 2002:
                val = False
        #iyr - four digits; at least 2010 and at most 2020.
        iyr = re.compile(r'iyr:\d\d\d\d')
        mo = iyr.search(passport)
        if not mo:
            val = False
        else:
            if int(mo.group()[4:]) < 2010 or int(mo.group()[4:]) > 2020:
                val = False
        #eyr - four digits; at least 2020 and at most 2030.
        eyr = re.compile(r'eyr:\d\d\d\d')
        mo = eyr.search(passport)
        if not mo:
            val = False
        else:
            if int(mo.group()[4:]) < 2020 or int(mo.group()[4:]) > 2030:
                val = False
        #hgt - a number followed by either cm or in, with bounds for each
        hgtcm = re.compile(r'hgt:\d\d\dcm')
        hgtin = re.compile(r'hgt:\d\din')
        mocm = hgtcm.search(passport)
        moin = hgtin.search(passport)
        if mocm is None and moin is None:
            val = False
        else:
            if mocm:
                if int(mocm.group()[4:7]) < 150 or int(mocm.group()[4:7]) > 193:
                    val = False
            if moin:
                if int(moin.group()[4:6]) < 59 or int(moin.group()[4:6]) > 76:
                    val = False
        #hcl - a # followed by exactly six characters 0-9 or a-f.
        hcl = re.compile(r'hcl:#[a-f0-9]{6}')
        mo = hcl.search(passport)
        if not mo:
            val = False
        
        #ecl - exactly one of: amb blu brn gry grn hzl oth.
        ecl = re.compile(r'ecl:blu|ecl:grn|ecl:hzl|ecl:oth|ecl:amb|ecl:gry|ecl:brn')
        mo = ecl.search(passport)
        if mo == None:
            val = False
        
        #pid - a nine-digit number, including leading zeroes 
        pid10 = re.compile(r'[0-9]{10}')
        pid = re.compile(r'[0-9]{9}')
        mo10 = pid10.search(passport)
        mo = pid.search(passport)
        if mo10 or not mo:
            val = False                        
        if val:
            # passed all tests
            valid += 1
    return valid


print(f'There are {passport_checker_pt2(passports)} valid passports in Part 2.')

# Attempt 1: 160 is too low, I'm eliminating too many valid passports.
# Attempt 2: 185 is too high
# LOL 184 is right - got it by knocking out a(n apparently lone) 10-digit-or-more pid
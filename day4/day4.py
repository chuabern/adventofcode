import re

with open("day4_input.txt", "r") as f:
    passports = list(f.read().split('\n\n'))

required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

def number_valid_passports(passports):
    valid_passports = 0
    exceptional_field = 'cid'
    for passport in passports:
        existing_fields = 0 
        for field in required_fields:
            if field in passport:
                existing_fields += 1

        if existing_fields == 8:
            valid_passports += 1
        elif existing_fields == 7 and exceptional_field not in passport:
            valid_passports += 1
    print("The number of valid passports are {}".format(valid_passports))
    return valid_passports

number_valid_passports(passports)

def number_valid_passports_new_condition(passports):
    valid_passports = 0
    exceptional_field = 'cid'
    for passport in passports:
        # print("loop1")
        fields = {}
        valid_fields = 0 
        passport_list = passport.split()
        for field in passport_list: #Cleaning the dictionary
            value = field.partition(":")[2]
            fields[field.partition(":")[0]] = value
        if 'byr' in fields.keys():
            if int(fields['byr']) >= 1920 and int(fields['byr']) <= 2002:
                valid_fields += 1
            else:
                continue # Can skip this passport since it already not fulfill this criteria
        else:
            continue

        if 'iyr' in fields.keys():
            if int(fields['iyr']) >= 2010 and int(fields['iyr']) <= 2020:
                valid_fields += 1
            else:
                continue
        else:
            continue

        if 'eyr' in fields.keys():
            if int(fields['eyr']) >= 2020 and int(fields['eyr']) <= 2030:
                valid_fields += 1
            else:
                continue
        else:
            continue

        if 'hgt' in fields.keys():
            if 'cm' in fields['hgt']:
                if int(fields['hgt'][:-2]) >= 150 and int(fields['hgt'][:-2]) <= 193:
                    valid_fields += 1
            elif 'in' in fields['hgt']:
                if int(fields['hgt'][:-2]) >= 59 and int(fields['hgt'][:-2]) <= 76:
                    valid_fields += 1
            else:
                continue
        else:
            continue

        if 'hcl' in fields.keys():
            if fields['hcl'][0] == '#':
                if len(fields['hcl'][1:]) == 6 and re.findall("[0-9a-f]", fields['hcl'][1:]):
                    valid_fields += 1
                else: 
                    continue
            else:
                continue
        else: 
            continue

        eye_colors = ['amb', 'blu' ,'brn', 'gry' ,'grn' ,'hzl' ,'oth']
        if 'ecl' in fields.keys():
            if any(color in fields['ecl'] for color in eye_colors):
                valid_fields += 1
            else: 
                continue
        else:
            continue

        if 'pid' in fields.keys():
            if len(fields['pid']) == 9 and re.findall("[0-9]", fields['pid']):
                valid_fields += 1
            else:
                continue
        else:
            continue

        if valid_fields == 7:
            valid_passports += 1

    print("The number of valid passports according to the new criteria is {}".format(valid_passports))

number_valid_passports_new_condition(passports)
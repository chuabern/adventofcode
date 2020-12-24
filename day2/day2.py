import csv

with open("day2_input.txt", "r") as f:
    passwords = list(f.read().split('\n'))

def validate_passwords(passwords):
    valid = 0
    invalid = 0
    for i in passwords:
        split = i.split(":")
        policy = split[0].partition(" ")[0]
        character = split[0].partition(" ")[2]
        password = split[1]

        lower_bound = policy.partition("-")[0]
        lower_bound = int(lower_bound)
        upper_bound = policy.partition("-")[2]
        upper_bound = int(upper_bound)
        character_count = password.count(character)

        if character_count >= lower_bound and character_count <= upper_bound:
            valid += 1 
        else:
            invalid += 1
    print("The number of valid passwords are {} and the number of invalid passwords are {}.".format(valid,invalid))
    return valid,invalid

validate_passwords(passwords)
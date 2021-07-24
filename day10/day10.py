import itertools
from itertools import permutations

with open('day10_input.txt', 'r') as text:
    lines = text.read().split("\n")

with open('testinput.txt', 'r') as text:
    lines = text.read().split("\n")

lines = list(map(int, lines)) # Convert all to int
all_numbers = sorted(lines)


### Part 1

number_of_1jolt_differences = 0
number_of_3jolt_differences = 0
starting_number = 0

for number in all_numbers:
    if all_numbers.index(number) == 0: # Most initial number
        difference = number - starting_number
    else:
        difference = number - all_numbers[all_numbers.index(number)-1]
    # print(difference)
    if difference == 1:
        number_of_1jolt_differences += 1
    elif difference == 3:
        number_of_3jolt_differences += 1

    # Final number in the list
    if all_numbers.index(number) == len(all_numbers)-1:
        number_of_3jolt_differences += 1

# print(number_of_1jolt_differences)
# print(number_of_3jolt_differences)

print(number_of_1jolt_differences*number_of_3jolt_differences)



### PART 2

steps = [1,2,3]
print("ALL NUMBERS", all_numbers)
permut = []
for i in range(len(all_numbers)):
    permut.extend(list(itertools.permutations(all_numbers, i+1)))

valid_combinations = 0 

def check_next_number(number, number_list):
    steps = [1,2,3]
    try:
        next_number = number_list[number_list.index(number)+1]
        if next_number - number in steps:
            return 1
        else:
            return 0
    except:
        return 0

final_number = 7
valid_combinations = []
for comb in permut:
    # print('combination', comb)

    # Check initial number:
    check = 0
    if comb[0] in [0,1,2,3]:
        # print("Valid starting combo")
        for number in comb[0:]:
            # print('number', number)
            # print(check_next_number(number, comb))
            check += check_next_number(number, comb)
        # print(check)
        if check == len(comb)-1 and comb[-1] == max(all_numbers):
            # The last element always has to be the highest
            valid_combinations.append(comb)

## Runtime is crazy!!! :-(
print(len(valid_combinations))
print(max(all_numbers))
import re 
from collections import defaultdict

with open('day7_input.txt', 'r') as text:
    all_the_bags = text.read().split(".\n")

######### Part 1

sample = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

bag_types = []
all_bags = {}

# Find out which bags contain shiny gold bags
for bag in all_the_bags:
    outside_bag = " ".join(bag.split()[:2]) # :2 is the first two words in the sentence
    inside_bags = bag[bag.index('contain')+8:]
    individual_inside_bags = inside_bags.split(', ')
    individual_inside_bags = [cnt.lstrip() for cnt in individual_inside_bags]
    individual_inside_bags = [" ".join(cont.split(" ")[:-1]) for cont in individual_inside_bags]
    individual_inside_bags = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in individual_inside_bags}
    if outside_bag not in bag_types:
        bag_types.append(outside_bag)
        all_bags[outside_bag] = individual_inside_bags




# Write a function to see if the current bag matches the wanted bag
def check_current_bag(bags, wanted_bag, current_bag):
    if current_bag == wanted_bag:
        return 1 # Current bag is the shiny gold bag
    if bags.get(current_bag) is None:
        return 0 # Current bag is the dead end (final bag)
    else: # If it's not the final bag, figure out what's inside it
        counts = []
        for key, value in bags[current_bag].items():
            counts.append(check_current_bag(bags, wanted_bag, key))
        # print(max(counts))
        return max(counts)

number = 0
wanted_bag = 'shiny gold'

for key, value in all_bags.items():
    if key != wanted_bag:
        number += check_current_bag(
            all_bags,
            wanted_bag,
            key
        )

# print(number)
######### Part 2

wanted_bag = 'shiny gold'
current_bag = 'shiny gold'
total_number = 0
# Find the total number of individual bags inside the shiny gold bag

def get_number_of_individual_bags(all_bags, wanted_bag, current_bag, total_number):
    if current_bag == wanted_bag:
        # print(all_bags[wanted_bag])
        for key, value in all_bags[wanted_bag].items():
            total_number += int(value)
            # print(total_number)
        return total_number

for key, value in all_bags.items():
    if key == wanted_bag:
        # We start with the shiny gold bag,
        # and get the number of individual bags in it
        get_number_of_individual_bags(all_bags, wanted_bag, current_bag, total_number)
        # After that we want to look at each individual bag
        # and repeat the process
        for inside_bag, number in value.items():
            # print(inside_bag)
            wanted_bag = inside_bag
            current_bag = inside_bag
            get_number_of_individual_bags(all_bags, wanted_bag, current_bag, total_number)
        # print(value)
        # for each_number in value.values():
        #     total_number += int(each_number)


print(total_number)
# Got help from https://dev.to/qviper/advent-of-code-2020-python-solution-day-7-5319

import re 
from collections import defaultdict

with open('day7_input.txt', 'r') as text:
    bags = text.read().split(".\n")

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


# print(bags)
collecting_bags = []
collecting_bags_count = 0

bag_types = []
all_bags = {}
# Find out which bags contain shiny gold bags
for bag in bags:
    outside_bag = " ".join(bag.split()[:2]) # :2 is the first two words in the sentence
    # print(outside_bag)
    inside_bags = bag[bag.index('contain')+8:]
    individual_inside_bags = inside_bags.split(', ')
    if any('shiny gold bag' in bag for bag in individual_inside_bags):
        print(bag)
        collecting_bags.append(outside_bag)
        collecting_bags_count += 1
    # print(individual_inside_bags)
    if outside_bag not in bag_types:
        bag_types.append(outside_bag)
    # if all_bags.get(outside_bag):


print(collecting_bags)
print(collecting_bags_count)



######### Part 2

import re 
from collections import defaultdict

with open('day7_input.txt', 'r') as text:
    bags = text.read().split(".\n")

# Part 1

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

for bag in bags:
    outside_bag = " ".join(bag.split()[:2]) # :2 is the first two words in the sentence
    # print(outside_bag)
    inside_bags = bag[bag.index('contain')+8:]
    individual_inside_bags = inside_bags.split(', ')
    if 'shiny gold bags' in individual_inside_bags:
        print("yes")
    # print(individual_inside_bags)
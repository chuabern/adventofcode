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

    if outside_bag not in bag_types:
        bag_types.append(outside_bag)
        all_bags[outside_bag] = individual_inside_bags


wanted_bag = 'shiny gold'
current_bag = bag_types[0]
# Write a function to see if the current bag matches the wanted bag
def check_current_bag(bags, wanted_bag, current_bag):
    print('bags', bags)
    if current_bag == wanted_bag:
        return 1 # Current bag is the shiny gold bag
    if bags[current_bag] == None:
        return 0 # Current bag is the dead end (final bag)
    else: # If it's not the final bag, figure out what's inside it
        counts = []
        for key in bags.get(current_bag):
            print(key)
            counts.append(check_current_bag(bags, wanted_bag, key))
            # print(counts)
        return max(counts)
        print('yes')

check_current_bag(all_bags, wanted_bag, current_bag)

print(current_bag)


######### Part 2

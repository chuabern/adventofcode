"""
    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags.

    i.e. 1 shiny = 2 red + 2 red * 2 orange + 2 red * 2 orange * 2 yellow + 
                  2 red * 2 orange * 2 yellow * 2 green + 2 red * 2 orange * 2 yellow * 2 green * 2 blue+
                  2 red * 2 orange * 2 yellow * 2 green * 2 blue * 2 dark violet + 
                  2 red * 2 orange * 2 yellow * 2 green * 2 blue * 2 dark violet * 0 dark violet
                = 2 + 2**2 + 2**3 + 2 ** 4 + 2 ** 5 + 2 ** 6
                = 126
"""
test_bags = {"shiny gold": {"dark red": 2},
            "dark red": {"dark orange": 2},
            "dark orange": {"dark yellow": 2},
            "dark yellow": {"dark green": 2},
            "dark green": {"dark blue": 2},
            "dark blue": {"dark violet": 2},
            "dark violet": 0}

my_bag = "shiny gold"
bags_contains = {}
test_bags=all_bags
for k, v in test_bags.items():
    bags_contains[k] = []
    try:
        for kk, vv in v.items():

            bags_contains[k]+=[kk]*int(vv)
    except:
        pass
c=0

def count_bags(current_bag):
    if current_bag==" " or bags_contains.get(current_bag) is None:
        return 0

    #print("key:", current_bag)
    cnt = len(bags_contains[current_bag])
    cnts = []
    for k in bags_contains[current_bag]:
        cnts.append(count_bags(k))    
    return sum(cnts)+cnt

print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")
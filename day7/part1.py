from collections import defaultdict


def get_rules(unparsed_list):
    rules = {}
    for line in unparsed_list:
        line_split = line.split(" contain ")
        bag_colour = line_split[0].split(" bags")[0]
        bag_colour_req_bags = {}
        if line_split[1].startswith("no other bags"):
            rules[bag_colour] = bag_colour_req_bags
            continue
        required_bags = line_split[1].replace(" bags", "bag").replace(" bag", "").replace("bag", "").replace(".",
                                                                                                             "").split(
            ", ")
        for bag in required_bags:
            bag_colour_req_bags[bag[2:]] = int(bag[0])
        rules[bag_colour] = bag_colour_req_bags
    return rules


def get_parent_containers_dict(rules):
    parents = defaultdict(set)
    for parent, children in rules.items():
        for child in children:
            parents[child].add(parent)
    return parents


def get_possible_colors_for_color(bag_color, parent_rules, possible_bag_colors):
    possible_bag_colors.add(bag_color)
    parent_colors = parent_rules[bag_color]
    if len(parent_colors) == 0:
        return possible_bag_colors
    for color in parent_colors:
        if color not in possible_bag_colors:
            possible_bag_colors.update(get_possible_colors_for_color(color, parent_rules, possible_bag_colors))
    return possible_bag_colors


def count_required_bags(bag_color, rules):
    child_bags = rules[bag_color]
    sum = 1
    for child_color, child_count in child_bags.items():
        sum += child_count * count_required_bags(child_color, rules)
    return sum


with open("input.txt", 'r') as data:
    rules = get_rules([line for line in data.read().split("\n")])

# part 1
parent_containers = get_parent_containers_dict(rules)
result = get_possible_colors_for_color('shiny gold', parent_containers, set())
print(len(result) - 1, result)

# part 2
result = count_required_bags('shiny gold', rules)
print(result - 1)

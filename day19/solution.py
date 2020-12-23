def pre_process_rules(rules):
    swap_done = True
    ready_rules = {}
    return rules


def is_valid(word, rules, i):
    rule_zero = rules[i]
    return False


with open("input.txt", 'r') as data:
    sections = data.read().split("\n\n")
    rules_section = sections[0]
    rules = [line.replace("\"", "").split(": ") for line in rules_section]
    words = sections[1].split("\n")

rules = pre_process_rules(rules)

# part 1
print(sum([is_valid(word, rules, 0) for word in words]))

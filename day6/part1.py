# part 1
print(sum([len(set(line.replace("\n", ""))) for line in open("input.txt", 'r').read().split("\n\n")]))

# part 2
print(sum([sum([all([answer in other_person_answers for other_person_answers in group_answers]) for answer in group_answers[0]]) for group_answers in [list(line.split("\n")) for line in open("input.txt", 'r').read().split("\n\n")]]))

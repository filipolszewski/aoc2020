from collections import deque


def play_game(cups, moves):
    len_cups = len(cups)
    cups_set = set(cups)
    max_elem = max(cups)
    next_elem_index = 0
    dest_index = 1

    for i in range(moves):
        if i % 1000 == 0:
            print(i)
        index = next_elem_index
        curr_elem = cups[index]

        n_1 = cups[(index + 1) % len_cups]
        n_2 = cups[(index + 2) % len_cups]
        n_3 = cups[(index + 3) % len_cups]
        next_elem_index = (index + 1) % len_cups

        cups.remove(n_1)
        cups.remove(n_2)
        cups.remove(n_3)

        removed_set = {n_1, n_2, n_3}

        potential_elem = curr_elem
        if cups[(dest_index - 1) % (len_cups - 3)] == potential_elem - 1:
            # print("Shortcut!")
            dest_index = (dest_index - 1) % (len_cups - 3)
        else:
            dest_elem = None
            while True:
                potential_elem -= 1
                if potential_elem not in cups_set:
                    potential_elem = max_elem
                if potential_elem in cups_set and potential_elem not in removed_set:
                    dest_elem = potential_elem
                    break
                else:
                    continue
            dest_index = cups.index(dest_elem)

        cups.rotate(-dest_index - 1)
        next_elem_index = (next_elem_index - dest_index - 1) % (len_cups - 3)
        cups.extend([n_1, n_2, n_3])

    return cups


def second():
    data.extend(range(10, 1000001))
    result = play_game(cups=data, moves=10000)
    index_1 = result.index(1)
    print(result[index_1 + 1] * result[index_1 + 2])


with open("input.txt", 'r') as data:
    data = deque([int(x) for x in data.read().split("\n")[0]])

# part 1
result = play_game(cups=data.copy(), moves=100)
result.rotate(len(result) - result.index(1))
print("".join([str(x) for x in result]))

# import cProfile
# import pstats
#
# cProfile.run("second()", "{}.profile".format(__file__))
# s = pstats.Stats("{}.profile".format(__file__))
# s.strip_dirs()
# s.sort_stats("time").print_stats(10)

second()

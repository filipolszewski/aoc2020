def get_from_seats_map(x, y, seats_map):
    if x < 0 or x >= len(seats_map[0]) or y < 0 or y >= len(seats_map):
        return "0"
    else:
        return seats_map[y][x]


def get_adjacent_occupied_seats_count(x, y, seats_map):
    occupied_cnt = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y):
                occupied_cnt += 1 if get_from_seats_map(i, j, seats_map) == "#" else 0
    return occupied_cnt


def get_closest_seat(x, y, x_d, y_d, seats_map):
    while True:
        x += x_d
        y += y_d
        square = get_from_seats_map(x, y, seats_map)
        if square != ".":
            return square


def get_eyesight_occupied_seats_count(x, y, seats_map):
    occupied_cnt = 0
    for i in (-1, 0, 1):
        for j in range(-1, 0, 1):
            if not (i == 0 and j == 0) and get_closest_seat(x, y, i, j, seats_map) == "#":
                occupied_cnt += 1
    return occupied_cnt


def floor_transform(x, y, seats_map):
    return False, '.'


def empty_seat_transform(x, y, seats_map):
    occupied_cnt = occupied_counter(x, y, seats_map)
    if occupied_cnt == 0:
        return True, "#"
    else:
        return False, "L"


def occupied_seat_transform(x, y, seats_map):
    occupied_cnt = occupied_counter(x, y, seats_map)
    if occupied_cnt >= tolerance:
        return True, "L"
    else:
        return False, "#"


def simulate_step(seats_map):
    changes_cnt = 0
    new_seats_map = []
    for y in range(len(seats_map)):
        row = []
        for x in range(len(seats_map[0])):
            changed, new_char = transforms[seats_map[y][x]](x, y, seats_map)
            row.append(new_char)
            changes_cnt += int(changed)
        new_seats_map.append(row)
    return changes_cnt > 0, new_seats_map


def count_taken_seats(seats_map):
    return "".join(["".join(row) for row in seats_map]).count("#")


def get_occupied_seats_after_stabilisation(seats_map):
    while True:
        map_changed, seats_map = simulate_step(seats_map)
        if not map_changed:
            break
    return count_taken_seats(seats_map)


with open("input.txt", 'r') as data:
    seat_map = [line.strip("") for line in data.read().split("\n")]

transforms = {'.': floor_transform, "#": occupied_seat_transform, "L": empty_seat_transform}

# Part 1
tolerance = 4
occupied_counter = get_adjacent_occupied_seats_count
print(get_occupied_seats_after_stabilisation(seat_map))

# Part 2

tolerance = 5
occupied_counter = get_eyesight_occupied_seats_count
print(get_occupied_seats_after_stabilisation(seat_map))

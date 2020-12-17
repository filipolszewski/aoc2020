def get_from_cube_map(x, y, z, cube_map):
    if x < 0 or x >= len(cube_map[0][0]) or y < 0 or y >= len(cube_map[0]) or z < 0 or z >= len(cube_map):
        return "."
    else:
        return cube_map[z][y][x]


def get_active_neighbours_count(x, y, z, cube_map):
    active_cnt = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if not (i == x and j == y and k == z):
                    active_cnt += 1 if get_from_cube_map(i, j, k, cube_map) == "#" else 0
    return active_cnt


def inactive_transform(x, y, z, cube_map):
    active_cnt = get_active_neighbours_count(x, y, z, cube_map)
    if active_cnt == 3:
        return "#"
    else:
        return "."


def active_transform(x, y, z, cube_map):
    active_cnt = get_active_neighbours_count(x, y, z, cube_map)
    if active_cnt in (2, 3):
        return "#"
    else:
        return "."


def simulate_step(cube_map, z_range, y_range, x_range):
    new_cube_map = []

    for z in z_range:
        plane = []
        for y in y_range:
            row = []
            for x in x_range:
                new_char = transforms[get_from_cube_map(x, y, z, cubes_map)](x, y, z, cube_map)
                row.append(new_char)
            plane.append(row)
        new_cube_map.append(plane)
    return new_cube_map


def count_active_cubes(cube_map):
    return "".join(["".join(["".join(row) for row in plane]) for plane in cube_map]).count("#")


def get_active_cubes_after_iterations(cube_map, iteration_count):
    z_range, y_range, x_range = [-1, len(cube_map) + 1], [-1, len(cube_map[0]) + 1], [-1, len(cube_map[0][0]) + 1]
    while iteration_count != 0:
        cube_map = simulate_step(cube_map, range(*z_range), range(*y_range), range(*x_range))
        iteration_count -= 1
        z_range[1] += 2
        y_range[1] += 2
        x_range[1] += 2
    return count_active_cubes(cube_map)


with open("test.txt", 'r') as data:
    cubes_map = [[line.strip("") for line in data.read().split("\n")]]

transforms = {"#": active_transform, ".": inactive_transform}

# Part 1
print(get_active_cubes_after_iterations(cubes_map, 6))

from collections import defaultdict

nav_dict = {"0": (0, 1), "1": (1, -1), "2": (-1, 1), "3": (0, -1), "4": (-1, 0), "5": (1, 0)}


def replace(param):
    return param.replace("ne", "0").replace("se", "1").replace("nw", "2") \
        .replace("sw", "3").replace("w", "4").replace("e", "5")


def get_tile_xy(tile):
    x, y = 0, 0
    for step in tile:
        x += nav_dict[step][0]
        y += nav_dict[step][1]
    return x, y


with open("input.txt", 'r') as data:
    tiles_to_flip = replace(data.read()).split("\n")

# part 1
black_count = 0
tile_is_black = defaultdict(lambda: False)
for tile in tiles_to_flip:
    tile_x, tile_y = get_tile_xy(tile)
    if tile_is_black[(tile_x, tile_y)]:
        black_count -= 1
        tile_is_black[(tile_x, tile_y)] = False
    else:
        black_count += 1
        tile_is_black[(tile_x, tile_y)] = True
print(black_count)


def get_black_neighbours_count(x, y, black_tiles_set):
    count = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if (x - i) != (y - j) and (i, j) in black_tiles_set:
                count += 1
    return count


def should_be_black(x, y, black_tiles_set):
    neighbours_count = get_black_neighbours_count(x, y, black_tiles_set)
    if (x, y) in black_tiles_set:
        return neighbours_count in (1, 2)
    else:
        return neighbours_count == 2


def run_simulation_step(map_bounds, black_tiles_set):
    new_black_tiles = set()
    x_bounds, y_bounds = map_bounds
    for x in range(*x_bounds):
        for y in range(*y_bounds):
            if should_be_black(x, y, black_tiles_set):
                new_black_tiles.add((x, y))
    return new_black_tiles


def get_bounds(flipped):
    min_x, min_y, max_x, max_y = 1000, 1000, 0, 0
    for t in flipped:
        t_x, t_y = t
        if t_x < min_x:
            min_x = t_x
        if t_x > max_x:
            max_x = t_x
        if t_y < min_y:
            min_y = t_y
        if t_y > max_y:
            max_y = t_y
    return (min_x - 2, max_x + 2), (min_y - 2, max_y + 2)


# part 2
black_tiles = {tile for tile in tile_is_black.keys() if tile_is_black[tile]}
for step in range(100):
    bounds = get_bounds(black_tiles)
    black_tiles = run_simulation_step(bounds, black_tiles)
print(len(black_tiles))

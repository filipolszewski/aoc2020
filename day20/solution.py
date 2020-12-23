class Tile:

    def __init__(self, tile_as_string):
        self.id = int(tile_as_string.split("\n")[0].split(" ")[1].replace(":", ""))
        self.content = tile_as_string.split("\n")[1:]
        self.top_wall = self.get_top_wall(self.content)
        self.right_wall = self.get_right_wall(self.content)
        self.bottom_wall = self.get_bottom_wall(self.content)
        self.left_wall = self.get_left_wall(self.content)
        self.walls = {0: self.top_wall, 1: self.right_wall,
                      2: self.bottom_wall,
                      3: self.left_wall}
        self.all_walls = self.top_wall + self.right_wall + self.bottom_wall + self.left_wall

    @staticmethod
    def get_top_wall(tile_content):
        return [int(tile_content[0], 2), int("".join(reversed(tile_content[0])), 2)]

    @staticmethod
    def get_right_wall(tile_content):
        print(tile_content)
        wall_as_str = "".join([line[-1] for line in tile_content])
        return [int(wall_as_str, 2), int("".join(reversed(wall_as_str)), 2)]

    @staticmethod
    def get_bottom_wall(tile_content):
        return [int(tile_content[-1], 2), int("".join(list(reversed(tile_content[-1]))), 2)]

    @staticmethod
    def get_left_wall(tile_content):
        wall_as_str = "".join([line[0] for line in tile_content])
        return [int(wall_as_str, 2), int("".join(reversed(wall_as_str)), 2)]


def wall_has_match(tile_wall, other_tile):
    for wall in other_tile.all_walls:
        if wall in tile_wall:
            return True
    return False


def count_walls_without_matches(tile, tiles):
    count = 0
    for side in [0, 1, 2, 3]:
        for other_tile in tiles:
            if tile.id != other_tile.id and wall_has_match(tile.walls[side], other_tile):
                count += 1
                break
    return count


with open("input.txt", 'r') as data:
    tiles = [Tile(line.strip()) for line in data.read().replace(".", "0").replace("#", "1").split("\n\n")]

# part 1
result = 1
for tile in tiles:
    if count_walls_without_matches(tile, tiles) == 2:
        result *= tile.id
print(result)

# part 2
starting_tile = tiles[40]
tiles_matched = 1
while tiles_matched != len(tiles):
    print()
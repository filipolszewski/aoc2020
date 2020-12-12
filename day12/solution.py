north, south, east, west = (0, -1), (0, 1), (1, 0), (-1, 0)
rotation_dict = {"R": {east: south, south: west, west: north, north: east},
                 "L": {east: north, north: west, west: south, south: east}}
direction_dict = {"N": north, "S": south, "E": east, "W": west}


def get_relative_pos(waypoint):
    relative_pos = [east, south]
    if waypoint[0] == 0 and waypoint[1] == 0:
        return waypoint
    if waypoint[0] < 0:
        relative_pos[0] = west
    if waypoint[1] < 0:
        relative_pos[1] = north
    return relative_pos


def rotate(move, waypoint):
    relative_pos = get_relative_pos(waypoint)
    new_dirs = (rotation_dict[move[0]][relative_pos[0]], rotation_dict[move[0]][relative_pos[1]])
    x, y = waypoint[0], waypoint[1]
    waypoint[0] = new_dirs[0][0] * abs(y)
    waypoint[1] = new_dirs[0][1] * abs(x)
    waypoint[0] += new_dirs[1][0] * abs(y)
    waypoint[1] += new_dirs[1][1] * abs(x)
    return waypoint


with open("input.txt", 'r') as data:
    moves = [(line[0], int(line[1:])) for line in data.read().split("\n")]

# part 1
x, y, orient = 0, 0, east
for move in moves:
    if move[0] == "F":
        x += move[1] * orient[0]
        y += move[1] * orient[1]
        continue
    if move[0] in "RL":
        for i in range(int(move[1] / 90)):
            orient = rotation_dict[move[0]][orient]
        continue
    x += direction_dict[move[0]][0] * move[1]
    y += direction_dict[move[0]][1] * move[1]

print(x, y, abs(x) + abs(y))

# part 2
x, y, waypoint = 0, 0, [10, -1]
for move in moves:
    if move[0] == "F":
        x += move[1] * (waypoint[0])
        y += move[1] * (waypoint[1])
        continue
    if move[0] in "RL":
        for i in range(int(move[1] / 90)):
            waypoint = rotate(move, waypoint)
        continue
    waypoint[0] += direction_dict[move[0]][0] * move[1]
    waypoint[1] += direction_dict[move[0]][1] * move[1]

print(x, y, abs(x) + abs(y))


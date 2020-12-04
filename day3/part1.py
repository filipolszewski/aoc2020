def count_trees_on_directory(lines, dx, dy):
    x, y, trees_cnt = 0, 0, 0
    while y < len(lines):
        if lines[y][x % len(lines[0])] == '#':
            trees_cnt += 1
        x += dx
        y += dy
    return trees_cnt


with open("input.txt", 'r') as data:
    map2d = [line.strip() for line in data.readlines()]

# part 1
print(count_trees_on_directory(map2d, 3, 1))

# part 2
result = 1
for trajectory in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    result *= count_trees_on_directory(map2d, *trajectory)
print(result)

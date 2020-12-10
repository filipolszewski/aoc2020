with open("input.txt", 'r') as data:
    sorted_jolts_list = sorted([int(line) for line in data.read().split("\n")])
    sorted_jolts_list.insert(0, 0)

# part 1
jolt_diffs = {1: 0, 2: 0, 3: 1}
for i, jolt in enumerate(sorted_jolts_list[:-1]):
    jolt_diffs[sorted_jolts_list[i + 1] - jolt] += 1

print(jolt_diffs, jolt_diffs[1] * jolt_diffs[3])

# part 2 - hacky solution - will not work for all possible inputs..
chunks, chunk_start, possible_routes = [], 0, 1

for i, jolt in enumerate(sorted_jolts_list):
    is_last = i == len(sorted_jolts_list) - 1
    if is_last or sorted_jolts_list[i + 1] - jolt == 3:
        chunks.append(sorted_jolts_list[chunk_start + 1:i])
        chunk_start = i + 1

for chunk in chunks:
    if len(chunk) in (1, 2):
        possible_routes *= pow(2, len(chunk))
    if len(chunk) == 3:
        possible_routes *= pow(2, len(chunk)) - 1

print(possible_routes)

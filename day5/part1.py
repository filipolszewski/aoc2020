with open("input.txt", 'r') as data:
    data_binary = data.read().replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0")

boarding_passes = [line for line in data_binary.split("\n")]
seat_ids = [int(boarding_pass, 2) for boarding_pass in boarding_passes]

# part 1
print(max(seat_ids))

# part 2
seat_ids = sorted(seat_ids)
for i, seat_id in enumerate(seat_ids):
    if min(seat_ids) < seat_id < max(seat_ids):
        if seat_ids[i + 1] - seat_id == 2:
            print(seat_id + 1)
            break

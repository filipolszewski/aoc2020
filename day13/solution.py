def find_uber_bus_from_pair(bus_1, bus_2):
    # We want to create a 'new bus' that represents two buses
    # So we look on what is the first & second time those buses align correctly
    # we save it as 'offset' and 'cycle_length'
    # delta of new bus is 0! (you can imagine that uber-buses depart longer than 1min)

    # bus -> (offset, bus ID (cycle_length), bus 'delta')
    cycle, cycle_start = False, None
    bus_2_relative_delta = bus_2[2] - bus_1[2]
    index = bus_1[0]
    while not cycle:
        bus_2_aligned = (index + bus_2_relative_delta) % bus_2[1] == 0
        if bus_2_aligned:
            if cycle_start is None:
                # start the cycle
                cycle_start = index
            else:
                # cycle found - we've got all we need
                return cycle_start, index - cycle_start, 0
        index += bus_1[1]


with open("input.txt", 'r') as data:
    bus_input = [line for line in data.read().split("\n")]

# part 1
# no explanation here
buses = [int(bus) for bus in bus_input[1].replace(",x", "").split(",")]
start_time = int(bus_input[0])
earliest_bus, wait_time = 1E9, 1E9
for bus in buses:
    bus_wait_time = bus - (start_time % bus)
    if bus_wait_time < wait_time:
        wait_time = bus_wait_time
        earliest_bus = bus
print(earliest_bus * wait_time)

# part 2

# get rid of 'x' and mark each bus with the expected 'delta time' from time t
# also each bus has offset 0 for now - later on we will have different offsets
buses = [bus for bus in bus_input[1].split(",")]
buses_with_deltas = []
for i, bus in enumerate(buses):
    if bus != "x":
        buses_with_deltas.append((0, int(bus), i))

# iterate over buses and 'add' them to the current_bus, making an 'uber_bus'
current_bus = buses_with_deltas[0]
for i in range(1, len(buses_with_deltas)):
    current_bus = find_uber_bus_from_pair(current_bus, buses_with_deltas[i])

# offset of uber bus -> the first time that all buses are aligned & first bus departs
print(current_bus[0])

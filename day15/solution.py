with open("input.txt", 'r') as data:
    starting_numbers = [int(number) for number in data.read().split(",")]

N = 30000000
last_place = {number: i for i, number in enumerate(starting_numbers)}
number = None
i = len(starting_numbers) - 1
while i != N - 1:
    if number is not None and number in last_place.keys():
        new_number = i - last_place[number]
    else:
        new_number = 0
    last_place[number] = i
    number = new_number
    i += 1

print(number)

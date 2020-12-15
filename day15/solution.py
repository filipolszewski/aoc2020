with open("input.txt", 'r') as data:
    starting_numbers = [int(number) for number in data.read().split(",")]

N = 30000000
last_place = {number: i for i, number in enumerate(starting_numbers)}
number = 0

for i in range(len(starting_numbers), N - 1):
    new_number = 0 if number not in last_place.keys() else i - last_place[number]
    last_place[number] = i
    number = new_number

print(number)

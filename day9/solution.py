def is_valid(number, numbers):
    for i, num_i in enumerate(numbers):
        for j, num_j in enumerate(numbers[i:]):
            if num_i != num_j and num_i + num_j == number:
                return True
    return False


def find_invalid_number(numbers):
    for index, number in enumerate(numbers):
        prev_numbers = numbers[index - 25:index]
        if index >= 25 and not is_valid(number, prev_numbers):
            return number


def find_contiguous_set(numbers, desired_sum):
    current_sum = 0
    for index, num in enumerate(numbers):
        current_sum += num
        if current_sum == desired_sum:
            return numbers[:index + 1]
        if current_sum > desired_sum:
            return None


def find_encryption_weakness(numbers, invalid_number):
    for index in range(len(number_list)):
        result = find_contiguous_set(number_list[index:], invalid_number)
        if result:
            return min(result) + max(result)


with open("input.txt", 'r') as data:
    number_list = [int(line) for line in data.read().split("\n")]

# part 1
invalid_number = find_invalid_number(number_list)
print(invalid_number)

# part 2
print(find_encryption_weakness(number_list, invalid_number))

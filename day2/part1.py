def entry_valid_according_to_old_system(line):
    password_entry = line.split(": ")
    password = password_entry[1]

    policy_entry = password_entry[0].split(" ")
    policy_char = policy_entry[1]

    policy_values = policy_entry[0].split("-")
    min_count, max_count = int(policy_values[0]), int(policy_values[1])

    return min_count <= password.count(policy_char) <= max_count


def logical_xor(a, b):
    return (a or b) and not (a and b)


def entry_valid_according_to_the_actual_system(line):
    password_entry = line.split(": ")
    password = password_entry[1]

    policy_entry = password_entry[0].split(" ")
    policy_char = policy_entry[1]

    policy_values = policy_entry[0].split("-")
    first_position, second_position = int(policy_values[0]) - 1, int(policy_values[1]) - 1

    char_on_first = password[first_position] == policy_char
    char_on_second = password[second_position] == policy_char

    return logical_xor(char_on_first, char_on_second)


def main():
    with open("input.txt", 'r') as data:
        lines = [line.strip() for line in data.readlines()]

    # part 1
    result = 0
    for line in lines:
        if entry_valid_according_to_old_system(line):
            result += 1
    print(result)

    # part 2

    result = 0
    for line in lines:
        if entry_valid_according_to_the_actual_system(line):
            result += 1
    print(result)

    return


if __name__ == "__main__":
    main()

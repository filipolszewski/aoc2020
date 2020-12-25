def transform(value, subject_number):
    return (value * subject_number) % 20201227


def transform_n_times(subject_number, n):
    value = 1
    for _ in range(n):
        value = transform(value, subject_number)
    return value


def transform_until(subject_number, expected_value):
    loop_size, value = 0, 1
    while value != expected_value:
        loop_size += 1
        value = transform(value, subject_number)
    return loop_size


with open("input.txt", 'r') as data:
    keys = data.read().split("\n")

door_loop_size = transform_until(7, int(keys[1]))
print(transform_n_times(int(keys[0]), door_loop_size))

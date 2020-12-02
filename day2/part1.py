def main():
    """ Main program """

    with open("input.txt", 'r') as data:
        report_lines = [int(line.strip()) for line in data.readlines()]

    # part 1
    needed_numbers = set()
    for i, number in enumerate(report_lines):
        if number in needed_numbers:
            print(number * (2020 - number))
        needed_numbers.add(2020 - number)

    # part 2
    for i in range(len(report_lines)):
        for j in range(len(report_lines)):
            for k in range(len(report_lines)):
                if i != j != k and (report_lines[i] + report_lines[j] + report_lines[k]) == 2020:
                    print(report_lines[i] * report_lines[j] * report_lines[k])
                    return
    return


if __name__ == "__main__":
    main()

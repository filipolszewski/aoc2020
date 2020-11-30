def main():
    """ Main program """

    with open("input.txt", 'r') as data:
        lines = [line.strip() for line in data.readlines()]
    print(lines)
    return 0


if __name__ == "__main__":
    main()

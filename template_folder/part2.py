
def main():
    """ Main program """

    with open("../template_folder/input.txt", 'r') as data:
        lines = [line.strip() for line in data.readlines()]

    return 0


if __name__ == "__main__":
    main()

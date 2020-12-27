import re


class A:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value * other.value)

    def __mul__(self, other):
        return A(self.value + other.value)


def substitute(string):
    return re.sub(r"([0-9])", r"A(\1)", string)


with open("input.txt", 'r') as data:
    expressions = [substitute(line.replace("*", "|").replace("+", "*").replace("|", "+")) for line in
                   data.read().split("\n")]

# part 2
print(sum([eval(expression, {"A": A}).value for expression in expressions]))

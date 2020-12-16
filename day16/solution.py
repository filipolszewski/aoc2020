import math


class InputParser:

    def read_input(self, file_name):
        with open(file_name, 'r') as data:
            sections = [line for line in data.read().split("\n\n")]
        return self._read_fields(sections[0]), self._read_ticket(sections[1]), self._read_other_tickets(sections[2])

    def _get_bound(self, bound):
        bound_split = bound.split("-")
        return int(bound_split[0]), int(bound_split[1])

    def _get_ticket(self, line):
        return [int(val) for val in line.split(",")]

    def _read_fields(self, fields_section):
        fields = {}
        for field_declaration in fields_section.split("\n"):
            field_name = field_declaration.split(": ")[0]
            bounds = [self._get_bound(bound_str) for bound_str in field_declaration.split(": ")[1].split(" or ")]
            fields[field_name] = Field(field_name, bounds)
        return fields

    def _read_ticket(self, your_ticket_section):
        return self._get_ticket(your_ticket_section.split("\n")[1])

    def _read_other_tickets(self, other_tickets_section):
        return [self._get_ticket(line) for line in other_tickets_section.split("\n")[1:]]


class Field:
    def __init__(self, name, bounds):
        self.name = name
        self.bounds = bounds

    def is_value_valid(self, value):
        for bound in self.bounds:
            if bound[0] <= value <= bound[1]:
                return True
        return False


# Part 1
def value_invalid(fields_list, value):
    for field in fields_list:
        if field.is_value_valid(value):
            return False
    return True


def first(fields, other_tickets):
    return sum([value if value_invalid(fields.values(), value) else 0 for ticket in other_tickets for value in ticket])


# Part 2
def get_possible_fields_for_column(fields_list, valid_tickets):
    # Iterate over all the ticket data and 'eliminate' fields that surely don't match to a column
    possible_fields_for_column = {index: fields_list[:] for index in list(range(len(valid_tickets[0])))}
    for ticket in valid_tickets:
        for index, value in enumerate(ticket):
            for field in possible_fields_for_column[index]:
                if not field.is_value_valid(value):
                    possible_fields_for_column[index].remove(field)
    return possible_fields_for_column


def remove_field_from_other_columns(possible_fields_for_column, field, column):
    for col in possible_fields_for_column.keys():
        if col != column and field in possible_fields_for_column[col]:
            possible_fields_for_column[col].remove(field)


def resolve_field_map(fields, valid_tickets):
    # Read the data and check what fields could be given to each column
    fields_list = list(fields.values())
    possible_fields_for_column = get_possible_fields_for_column(fields_list, valid_tickets)

    # -> check what columns have only 1 field match
    # -> choose that column for the field and remove that field for other columns
    # -> repeat the process until all fields have their columns matched
    field_map = {}
    while len(field_map.items()) != len(fields):
        for column, fields in possible_fields_for_column.items():
            if len(fields) == 1:
                field = fields[0]
                field_map[field.name] = column
                remove_field_from_other_columns(possible_fields_for_column, field, column)
    return field_map


def ticket_valid(fields, ticket):
    for value in ticket:
        if value_invalid(fields, value):
            return False
    return True


def second(fields, ticket, other_tickets):
    valid_tickets = [t for t in other_tickets if ticket_valid(fields.values(), t)]
    field_map = resolve_field_map(fields, valid_tickets)
    return math.prod([ticket[index] for field_name, index in field_map.items() if "departure" in field_name])


def main():
    fields, ticket, other_tickets = InputParser().read_input("input.txt")
    print(first(fields, other_tickets))
    print(second(fields, ticket, other_tickets))


if __name__ == "__main__":
    main()

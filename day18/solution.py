def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def solve_no_precedence(expression):
    expr_stack = []
    expr, operator = 0, add
    for char in expression:
        if char == '(':
            expr_stack.append((operator, expr))
            expr, operator = 0, add
            continue
        if char == ')':
            operator, last_expr = expr_stack.pop()
            expr = operator(expr, last_expr)
            continue
        if char == '+':
            operator = add
            continue
        if char == '*':
            operator = mul
            continue
        expr = operator(expr, int(char))
    return expr


with open("input.txt", 'r') as data:
    expressions = [line.replace(" ", "") for line in data.read().split("\n")]

# part 1
print(sum([solve_no_precedence(expression) for expression in expressions]))

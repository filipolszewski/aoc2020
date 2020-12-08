def parse_program(program_lines):
    parsed_lines = []
    for line in program_lines:
        split = line.split(" ")
        parsed_lines.append([split[0], int(split[1])])
    return parsed_lines


def nop_inst(arg, pc, acc):
    return pc + 1, acc


def acc_inst(arg, pc, acc):
    return pc + 1, acc + arg


def jmp_inst(arg, pc, acc):
    return pc + arg, acc


instruction_map = {'nop': nop_inst, 'acc': acc_inst, 'jmp': jmp_inst}


def run_program_until_loop(program_lines):
    pc, acc, executed_lines = 0, 0, set()

    while 0 <= pc < len(program_lines) and pc not in executed_lines:
        executed_lines.add(pc)
        print(pc)
        line = program_lines[pc]
        pc, acc = instruction_map[line[0]](line[1], pc, acc)

    return pc, acc


with open("input.txt", 'r') as data:
    lines = [line.strip() for line in data.read().split("\n")]
    program = parse_program(lines)

# part 1
print(run_program_until_loop(program))

# part 2
pc, acc = 0, 0
swap_dict = {"nop": "jmp", "jmp": "nop"}

for line in program:
    if line[0] in swap_dict.keys():
        line[0] = swap_dict[line[0]]
        pc, acc = run_program_until_loop(program)
        line[0] = swap_dict[line[0]]
        if pc == len(program):
            break

print(acc)

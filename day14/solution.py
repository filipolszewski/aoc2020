import re
from itertools import chain, combinations


def read_mem_instruction(instr):
    instr_split = re.findall(r'\d+', instr)
    return int(instr_split[0]), int(instr_split[1])


def set_bit(value, bit_val, bit_pos):
    if bit_val == '1':
        return value | (1 << bit_pos)
    if bit_val == '0':
        return value & ~(1 << bit_pos)
    return value


def set_bit_v2(value, bit_val, bit_pos):
    if bit_val == '1':
        return value | (1 << bit_pos)
    return value


def get_masked_value(value, bit_mask, bit_setter=set_bit):
    for i, bit_val in enumerate(reversed(bit_mask)):
        value = bit_setter(value, bit_val, i)
    return value


def all_subsets(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_masked_addresses(address, bit_mask):
    # apply mask with new rules
    address = get_masked_value(address, bit_mask, set_bit_v2)
    # generate all addresses
    address_list = []
    floating_bits = [35 - i for i, ltr in enumerate(bit_mask) if ltr == 'X']
    for bits_to_set in all_subsets(floating_bits):
        for bit_pos in floating_bits:
            value = '1' if bit_pos in bits_to_set else '0'
            address = set_bit(address, value, bit_pos)
        address_list.append(address)
    return address_list


with open("input.txt", 'r') as data:
    init_program = [line for line in data.read().split("\n")]

# part 1
memory = {}
for line in init_program:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        continue
    index, val = read_mem_instruction(line)
    memory[index] = get_masked_value(val, mask)
print(sum(memory.values()))

# part 2
memory = {}
for line in init_program:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        continue
    index, val = read_mem_instruction(line)
    addr_list = get_masked_addresses(index, mask)
    for addr in addr_list:
        memory[addr] = val

print(sum(memory.values()))

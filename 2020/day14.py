import re

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

# Part A
mask = ""
mem = {}
for line in input:
    if "mask" in line:
        mask = line.split("=")[1].strip()
    else:
        match = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
        index = int(match.group(1))
        value = int(match.group(2))
        
        for i, bit in enumerate(mask[::-1]):
            if bit == '1':
                value = value | (1 << i)
            elif bit == '0':
                value = value & ~(1 << i)

        mem[index] = value

mem_sum = 0
for index in mem:
    mem_sum += mem[index]

print(mem_sum)

# Part B
mask = ""
mem = {}
for line in input:
    if "mask" in line:
        mask = line.split("=")[1].strip()[::-1]
    else:
        match = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
        index = int(match.group(1))
        value = int(match.group(2))
        
        x_count = 0
        for i, bit in enumerate(mask):
            if bit == '1':
                index = index | (1 << i)

            elif bit == 'X':
                x_count += 1

        for number in range(2**x_count):
            temp_index = index
            x_bit_num = 0
            for i, bit in enumerate(mask):
                if bit == 'X':
                    if number & (1 << x_bit_num):
                        temp_index = temp_index | (1 << i)
                    else:
                        temp_index = temp_index & ~(1 << i)
                    x_bit_num += 1 

            mem[temp_index] = value

mem_sum = 0
for index in mem:
    mem_sum += mem[index]

print(mem_sum)
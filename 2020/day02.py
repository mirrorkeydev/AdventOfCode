with open('input.txt', 'r') as f:
    input = [line.strip() for line in f]

num_valid = 0

for line in input:
    min = int(line.split('-')[0])
    rest = line.split('-')[1]
    max = int(rest.split(' ')[0])
    rest = rest.split(' ')[1]
    target_char = rest[0]
    string = line.split(':')[1].strip()
    
    if ((string[min-1] == target_char and string[max-1] != target_char) or 
        (string[min-1] != target_char and string[max-1] == target_char)):
        num_valid += 1

print(num_valid)


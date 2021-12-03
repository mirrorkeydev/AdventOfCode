# Part 1:

f = open("input.txt", "r")
lines = f.readlines()
arr = []
for line in lines:
  arr.append(line[:-1])

gamma_rate = ""
epsilon_rate = ""

for i in range(len(arr[0])):
  num_1s = len([x[i] for x in arr if x[i] == "1"])
  num_0s = len([x[i] for x in arr if x[i] == "0"])

  if num_1s > num_0s:
    gamma_rate += "1"
    epsilon_rate += "0"
  else:
    gamma_rate += "0"
    epsilon_rate += "1"

print(int(gamma_rate, 2)*int(epsilon_rate, 2))

# Part 2:

f = open("input.txt", "r")
lines = f.readlines()
arr = []
for line in lines:
  arr.append(line[:-1])

def find_array_number(og_arr, a, b):
  i = 0
  arr = [*og_arr]
  while len(arr) > 1:
    num_1s = len([x[i] for x in arr if x[i] == "1"])
    num_0s = len([x[i] for x in arr if x[i] == "0"])
    if num_1s >= num_0s:
      arr = [x for x in arr if x[i] == a]
    else:
      arr = [x for x in arr if x[i] == b]
    i += 1
  return arr[0]

oxygen = find_array_number(arr, "1", "0")
co2 = find_array_number(arr, "0", "1")

print(int(oxygen, 2)*int(co2, 2))

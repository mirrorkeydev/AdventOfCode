f = open("input.txt", "r")
lines = f.readlines()

arr = []

for line in lines:
  arr.append(int(line))

for num in arr:
  for num2 in arr:
    for num3 in arr:
      if num + num2 + num3 == 2020:
        print(num*num2*num3)
f = open("input.txt", "r")
lines = f.readlines()

arr = []

for line in lines:
  arr.append(int(line))

count = 0

window_sum = arr[0] + arr[1] + arr[2]
for i in range(1, len(arr)-2):
  window_sum_2 = arr[i] + arr[i+1] + arr[i+2]
  if window_sum_2 > window_sum:
    count += 1
  window_sum = window_sum_2

print(count)

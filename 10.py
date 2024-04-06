prev_temp = float(input())
count = 0

while True:
    temp = float(input())
    if temp == 0:
        break
    if temp < prev_temp:
        count += 1
    prev_tempe = temp

print(count)

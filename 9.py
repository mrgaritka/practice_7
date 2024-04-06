n, r, k = map(int, input().split())
day = 1

while n + (n*k*0.01) < r:
  day += 1
  n = n + (n*k*0.01)
print(day+1)

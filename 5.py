N = int(input())
for i in range(1, int(N**0.4)):
  if i**3 <= N:
    print(i**3, end = ' ')

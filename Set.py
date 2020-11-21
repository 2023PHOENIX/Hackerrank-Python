N = int(input())

s = set()
for i in range(N):
    s.add(input())

c = 0
for _ in s:
    c += 1
print(s)

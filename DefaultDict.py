n = int(input())
m = int(input())
l1 = list()
l2 = list()

for i in range(n):
    l1.append(int(input()))
for i in range(m):
    l2.append(int(input()))

from collections import defaultdict
d = defaultdict(l1)

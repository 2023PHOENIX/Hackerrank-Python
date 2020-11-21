# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list

N = int(input())
L = []

for i in range(N):
    n = input().split()
    if n[0] == 'insert':
        L.insert(int(n[1]),int(n[2]))
    elif n[0] == 'print':
        print(L)
    elif n[0] == 'append':
        L.append(int(n[1]))
    elif n[0] == 'remove':
        L.remove(int(n[1]))
    elif n[0] == 'sort':
        L.sort()
    elif n[0] == "pop":
        L.pop()
    elif n[0] == 'reverse':
        L.sort(reverse=True)
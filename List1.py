N = int(input())

arr = list()
for i in range(N):
    choice = input().split()
    if choice[0]=='insert':
        arr.insert(int(choice[1]),int(choice[2]))
    elif choice[0] = 'append':
        arr.append(int(choice[1]))
    elif choice[0] == 'remove'
        arr.remove(int(choice[1]))
    elif choice[0] == 'print'
        print(arr)
    elif choice[0] = 'sort':
        print(arr.sort())
    elif choice[0] = 'reverse':
        print(arr.sort(reverse=True))
    elif choice[0] = 'pop':
        print(arr.pop())
        

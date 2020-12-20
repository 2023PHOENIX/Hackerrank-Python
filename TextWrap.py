S = input()
n = int(input())

result = [(S[i:i+n]) for i in range(0,len(S),n)]

print(result)

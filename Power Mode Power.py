# You are given three integers: , , and , respectively. Print two lines.
# The first line should print the result of pow(a,b).
# The second line should print the result of pow(a,b,m).


def power(a, b, n):
    return pow(a, b) % n


a = int(input())
b = int(input())
c = int(input())

print(pow(a, b))
print(power(a, b, c))

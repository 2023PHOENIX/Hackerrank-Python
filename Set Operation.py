# .remove(x)
# This operation removes element  from the set.
# If element  does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.remove(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.remove(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.remove(0)
# KeyError: 0
# .discard(x)
# This operation also removes element  from the set.
# If element  does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.discard(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.discard(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.discard(0)
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
#
# Example
#
# >>> s = set([1])
# >>> print s.pop()
# 1
# >>> print s
# set([])
# >>> print s.pop()
# KeyError: pop from an empty set
# Task
# You have a non-empty set , and you have to execute  commands given in  lines.
#
# The commands will be pop, remove and discard.
S = set()
N = int(input())

string = input().split(' ')

for i in string:
    S.add(i)

op = int(input())

for i in range(op):
    ch = input().split(' ')
    if ch[0] == 'pop':
        S.pop()
    elif ch[0] == 'remove':
        S.remove(ch[1])
    elif ch[0] == 'discard':
        S.discard(ch[1])


print(int(S))




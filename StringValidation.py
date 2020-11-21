# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#
# >>> print 'ab123'.isalnum()
# True
# >>> print 'ab123#'.isalnum()
# False
# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#
# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False
# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
#
# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False
# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
#
# >>> print 'abcd123#'.islower()
# True
# >>> print 'Abcd123#'.islower()
# False
# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).
#
# >>> print 'ABCD123#'.isupper()
# True
# >>> print 'Abcd123#'.isupper()
# False
# Task
#
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

str = input()

alpanum,alpha,digit,lower,upper = False, False, False, False, False

for i in str:
    if i.isalnum():
        alpanum = True
    if i.isalpha():
        alpha = True       # check only for one digit weather it is alpha or not
    if i.isdigit():
        digit = True
    if i.islower():
        lower = True
    if i.isupper():
        upper = True
print(alpanum)
print(alpha)
print(digit)
print(lower)
print(upper)

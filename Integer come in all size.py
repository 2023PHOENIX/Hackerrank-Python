# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).
#
# As we know, the result of  grows really fast with increasing .
#
# Let's do some calculations on very large integers.

#
# 9
# 29
# 7
# 27
# 4710194409608608369201743232


a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Print the result of a^b + c ^d on one line.


print(pow(a, b) + pow(c, d))

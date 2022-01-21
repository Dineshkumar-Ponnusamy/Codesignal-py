#You would like to write a function that takes integer numbers x, y, L and R as parameters, and returns True if xy lies within the interval (L, R] and False otherwise. You're considering several different ways to write the conditional statement inside this function:

if L < x ** y <= R:
if x ** y > L and x ** y <= R:
if x ** y in range(L + 1, R + 1):
#Which option would be the most efficient in terms of execution time?

# Option1, since doesn't have and or range operations.

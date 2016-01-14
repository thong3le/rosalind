from math import factorial
from itertools import permutations

n = input()
print factorial(n)
for p in permutations(range(1, n+1)):
	for i in p:
		print i,
	print 
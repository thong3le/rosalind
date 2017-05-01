# Author: Thong Le
# Date: 
#
# rosalind.info PERM - Enumerating Gene Orders
#
# Solution Approach: 
#
#
#

from math import factorial
from itertools import permutations

n = input()
print factorial(n)
for p in permutations(range(1, n+1)):
	for i in p:
		print i,
	print 
# Author: Thong Le
# Date: 
#
# rosalind.info SUBS - Finding a Motif in DNA
#
# Solution Approach: 
#
#
#

s1 = raw_input()
s2 = raw_input()

m = len(s1)
n = len(s2)

for i in range(m-n+1):
	for j in range(n):
		if s1[i+j] != s2[j]:
			break
	else:
		print i+1,
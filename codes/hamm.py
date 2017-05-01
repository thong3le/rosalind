# Author: Thong Le
# Date: 
#
# rosalind.info HAMM - Counting Point Mutations
#
# Solution Approach: 
#
#
#

s1 = raw_input()
s2 = raw_input()

def hamming(s, t):
    return len(filter(lambda pair: pair[0]!=pair[1], zip(list(s),list(t))))

count = 0

for i in range(len(s1)):
	if s1[i] != s2[i]:
		count += 1

print count
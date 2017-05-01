f = open('raw_names.txt', 'r')

problems = []

for line in f.readlines():
	line = line.strip()
	if len(line) > 0:
		words = line.split()
		problems.append((words[0], ' '.join(words[1:-1])))

def print_out_names():
	for p in problems:
		name = '[{}][{}]'.format(p[1], p[0].lower())
		print "| {:5}| {:70} \[ [solution][{}_py] \]".format(p[0], name, p[0].lower())

def print_out_links():
	for p in problems:
		print "[{}]: http://rosalind.info/problems/{}/".format(p[0].lower(), p[0].lower())
		print "[{}_py]: https://github.com/thongle91/rosalind/tree/master/codes/{}.py".format(p[0].lower(), p[0].lower())


def create_files():
	for p in problems:
		fn = '../codes/{}.py'.format(p[0].lower())
		f = open(fn, 'w')
		content = "# Author: Thong Le\n# Date: \n#\n# rosalind.info {} - {}\n#\n".format(p[0], p[1])
		content += "# Solution Approach: \n#\n#\n#\n"
		f.write(content)

create_files()
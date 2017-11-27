import re
from itertools import groupby

def decode(string) : 
	groups = re.findall('(\d*\D{1})', string)
	pairs = map(lambda g: [re.match('\d*', g).group(), g[-1]], groups)
	# Fix hardcoded 0 and 1 indices
	# Also change name of x variable
	return ''.join(map(lambda x: int(x[0]) * x[1] if x[0].isdigit() else x[1], pairs))

def encode(string):
	return ''.join(map(lambda g: helper(g), [list(g) for k, g in groupby(string)]))

	# s=''

	# for ctr in string : 
	# 	nb=string.count(ctr)
	# 	if ctr in s : 
	# 		pass 
	# 	else : 
	# 		if nb==1 :
	# 			s+='%s'%(ctr)
	# 		else : 
	# 			s+='%s%s'%(nb,ctr)

	# return s

def helper(g):
	return g[0] if len(g) == 1 else str(len(g)) + g[0]
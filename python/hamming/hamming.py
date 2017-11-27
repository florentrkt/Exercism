def distance(strand_a, strand_b):

	count=0

	if len(strand_a) != len(strand_b) :
		raise ValueError ('Not comparable')

	else : 
		x=0
		while x < len(strand_a) :
			if strand_a[x] != strand_b[x] :
				count+=1
				x+=1
			else : 
				x+=1

	return count

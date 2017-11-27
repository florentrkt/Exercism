def sieve(limit):
	liste=[]
	for x in range(2,limit+1) :
		liste_copy=[]
		for y in range(2,limit+1) :
			if x%y==0:
				liste_copy.append(y)
		if len(liste_copy) == 1 : 
			liste.append(x)
	return liste

# if __name__ == '__main__':
#     print(sieve(10))


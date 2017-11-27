def sum_of_multiples(limit, multiples):

	"""
		C'est une fonction qui retourne la somme des multiples 
		d'une liste de nombre introduit dans le paramètre : multiples. 

		Cette somme ne prend pas en compte les doublons. 

	"""

	l=list(range(0,limit))
	result=[]
	for value in multiples : 
		for number in l : 
			if number%value == int() : 
				result.append(number)

	return sum(set(result))

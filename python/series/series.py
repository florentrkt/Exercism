def slices(series, length):
	"""
	Given a string of digits, output all the contiguous
	 substrings of length n in that string.
	For example, the string "49142" has the following 3-digit series:
	    491
	    914
	    142
	"""

	result=[]

	if len(series) < length or length==0 : 
		raise ValueError

	length_copy=length #because of the condition in line 15
	for index, value in enumerate(series) : 
		liste=[]
		series_values=series[index:length_copy]
		length_copy+=1
		for x in series_values : 
			liste.append(int(x))
		if len(liste) == length :
			result.append(liste)
	
	return result
	# numbers = [int(digit) for digit in series]
	# print(numbers)
	# if length <= 0 or length > len(series):
	# 	raise ValueError
	# # return [numbers[i:i + length] for i in range(len(numbers) - length + 1)]
	# for i in range(len(numbers)-length+1) : print(i)


		



# if  __name__ == '__main__' :
# 	print(slices("97867564", 3))
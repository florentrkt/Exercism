import string

def rotate(text, key):
	"""
	The Caesar cipher is a simple shift cipher that relies on 
	transposing all the letters in the alphabet 
	using an integer key between 0 and 26. 
	Using a key of 0 or 26 will always yield 
	the same output due to modular arithmetic. 
	The letter is shifted for as many values as 
	the value of the key.
	"""

	x=string.ascii_uppercase
	y=string.ascii_lowercase

	result=''

	for char in text : 
		if char.islower() :
			index=y.index(char)+int(key)
			if index >= 26 :
				index-=26
				char=y[index]
				result+=char
			else :
				char=y[index]
				result+=char
		elif char.isupper() :
			index=x.index(char)+int(key)
			if index >= 26 :
				index-=26
				char=x[index]
				result+=char
			else :
				char=x[index]
				result+=char
		elif char.isalpha()==False :
			result+=char
		else : 
			pass

	return result


def derotate(text, key):

	x=string.ascii_uppercase
	y=string.ascii_lowercase

	result=''

	for char in text : 
		if char.islower() :
			index=y.index(char)-int(key)
			if index < 0 :
				index+=26
				char=y[index]
				result+=char
			else :
				char=y[index]
				result+=char
		elif char.isupper() :
			index=x.index(char)-int(key)
			if index < 0 :
				index+=26
				char=x[index]
				result+=char
			else :
				char=x[index]
				result+=char
		elif char.isalpha()==False :
			result+=char
		else : 
			pass
	return result

if __name__ == '__main__' :
	print(derotate("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",13))




def hey(string):

	index = len(string) - 1
	s=string.split()

	# if string[index] == "?" :
	# 	return "Sure."

	# if string.isupper() == True :
	# 	return "Whoa, chill out!"

	# if string == " " :
	# 	return "Fine. Be that way!"

	# else : 
	# 	return "Whatever."

	if string.isupper() == True :
		return "Whoa, chill out!"


	if string.split() == [] :
		return "Fine. Be that way!"

	if string[index] == "?" or "?" in s[len(s)-1] :
		return "Sure."

	else : 
		return "Whatever."

	



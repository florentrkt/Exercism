def is_pangram(sentence):
	
	import string

	liste=[]
	for ctr in sentence.lower() : 
		if ctr in string.ascii_lowercase :
			liste.append(ctr)
		else :
			pass

	if len(set(liste))==len(string.ascii_lowercase):
		return True
	else : 
		return False

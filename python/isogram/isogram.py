import string

def is_isogram(str):
	liste=[]
	for ctr in str.lower():
		if ctr in string.ascii_lowercase :
			liste.append(ctr)
		else : 
			pass

	if len(set(liste))==len(liste):
		return True
	else :
		return False

	

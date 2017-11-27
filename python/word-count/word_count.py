import string

def word_count(phrase):

	chaine=''
	for ctr in phrase.lower() :
		if ctr.isalnum() == True :
			chaine+=ctr
		else :
			chaine+=' '
			pass
	
	d={}
	for elt in chaine.split() :
		nb=chaine.split().count(elt)
		if nb not in d :
			d[elt]=nb
		else : 
			pass

	return d


	# return chaine

# if __name__ == '__main__':
# 	word_count('rah rah ah ah ah\nroma roma ma\n'
#                        'ga ga oh la la\nwant your bad romance')

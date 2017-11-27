from rotational_cipher import rotate
import string

text=input('Mot à coder : ')
x=0
while x==0:
	key=input('Saisissez un chiffre entre [0,26] (à retenir pour le décodage) : ')
	try:
		key=int(key)
		x=1
	except ValueError :
		x=0
	if not 0<=key<=26 :
		x=0

rotate(text,key)
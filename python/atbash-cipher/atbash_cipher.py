import string

def encode(plain_text):
	
	a=[string.ascii_lowercase[::-1][string.ascii_lowercase.index(x)] 
	if x.isalpha() else x for x in plain_text.lower() if x.isalnum()]

	x=0
	s=''
	while x<len(a) :
		s+=''.join(a[x:x+5])
		s+=' '
		x+=5
	return s[:len(s)-1]



def decode(ciphered_text):

	b=[string.ascii_lowercase[string.ascii_lowercase[::-1].index(x)] 
	if x.isalpha() else x for x in ciphered_text.lower() if x.isalnum()]
	
	return ''.join(b)


    


# if __name__ == '__main__' :
# 	encode("The quick brown fox jumps over the lazy dog.")


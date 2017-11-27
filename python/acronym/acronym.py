import re

def abbreviate(words):
    return ''.join(x[0].upper() for x in re.findall(r"[\w']+", words))
    #return ''.join(map(lambda x: x[0].upper(), re.findall(r"[\w']+", words)))

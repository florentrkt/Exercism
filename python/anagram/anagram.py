# def detect_anagrams(word, candidates):
#     result=[]
#     for element in candidates : 
#         mot=''
#         if element.lower()==word.lower():
#             mot=''
#             break
#         if len(element) == len(word) :
#             for character in element : 
#                 # if element.count(character)!=word.count(character):
#                 #     mot=''
#                 #     break
#                 if character.lower() in word.lower() : 
#                     mot+=character
#                 else : 
#                     mot=''
#                     break 
#         if mot!='':
#             result.append(mot)
#     return result



def detect_anagrams(word, candidates):
    sort_word = sorted(word.lower())
    return [a for a in candidates if sorted(a.lower()) == sort_word and a.lower() != word.lower()]



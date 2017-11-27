import re

def say(number) :

    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty', \
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', \
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty',

          100 : 'one hundred',

          1000 : 'one thousand'

          }

    if number < 0 :
        raise AttributeError


    if number in d : 
        return d[number]

    if number in range(21, 100) : 
        l = list(map(int,str(number))) # for example 21 = [2, 1]
        num1 = int(str(l[0])+'0') # so num1 = 20
        num2 = int(l[-1]) # and num2 = 1
        if num2 == 0 : # for example 50,60, 70, ... 
            return d[num1]
        else : 
            return '%s-%s'%(d[num1],d[num2])

    if number > 1000 :
        number_trans = format(number, ',d')
        re.findall(r"(,)", number_trans)
        # A continuer








    # if number in range(100, 1000) :
    #     l = list(map(int,str(number)))
    #     num1=l[0]
    #     num2=l[1]
    #     num3=l[len(l)-1]
    #     if number in d :
    #         return d[number]
    #     if num2 == 0 :
    #         return d[num1]+' hundred and '+d[num3]
    #     else : 
    #         num4=int(str(num2)+str(num3))
    #         if num4<20 : 
    #             return d[num1]+' hundred and '+d[num4]
    #         else : 
    #             num2 = int(str(l[1])+'0')
    #             if num3 == 0 : # for example 50,60, 70, ... 
    #                 return d[num1]+' hundred and '+d[num2]
    #             else : 
    #                 return d[num1]+' hundred and '+d[num2]+'-'+d[num3]


    # if number in range(1000,10000) :
    #     l = list(map(int,str(number)))
    #     num1=l[0]
    #     num2=l[1]
    #     num3=l[2]
    #     num4=l[len(l)-1]
    #     if number in d : 
    #         return d[number]
    #     if num2 == 0 and num3==0 : 
    #         return d[num1]+' thousand and '+d[num4]
    #     if num2 == 0 and int(str(num3)+str(num4))<20 : 
    #         return d[num1]+' thousand and '+d[int(str(num3)+str(num4))]
    #     if num2 == 0 and int(str(num3)+str(num4))> 20 : 
    #         return  d[num1]+' thousand and '+d[int(str(l[2])+'0')]+'-'+d[num4]
    #     else : 
    #         x=l.pop(0)
    #         num1=l[0]
    #         num2=l[1]
    #         num3=l[len(l)-1]
    #         num4=int(str(num2)+str(num3))
    #         if num4<20 : 
    #             return d[x]+' thousand '+d[num1]+' hundred and '+d[num4]
    #         else : 
    #             num2 = int(str(l[1])+'0')
    #             if num3 == 0 : # for example 50,60, 70, ... 
    #                 return d[x]+' thousand '+d[num1]+' hundred and '+d[num2]
    #             else : 
    #                 return d[x]+' thousand '+d[num1]+' hundred and '+d[num2]+'-'+d[num3]

            
if __name__ == '__main__' :
    print(say(1234567890))



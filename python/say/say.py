import re

def say(number) :

    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty', \
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', \
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty',

          100 : 'one hundred'}

    k = 1000
    m = k * 1000 
    b = m * 1000
    t = b * 1000

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

    if number < k : 
        if number%100 == 0 : 
            return d[number//100] + ' hundred'
        else : 
            return d[number//100] + ' hundred and ' + say(number%100)

    if number < m : 
        if number%k == 0 : 
            return say(number//k) + ' thousand'
        else : 
            return say(number//k) + ' thousand ' + say(number%k)

    if number < b : 
        if number%m == 0 : 
            return say(number//m) + ' million'
        else : 
            return say(number//m) + ' million ' + say(number%m)

    if number < t : 
        if number%b == 0 : 
            return say(number//b) + ' billion'
        else : 
            return say(number//b) + ' billion ' + say(number%b)

    raise AttributeError('num is too large: %s' % str(number))
    #intéréssant l'utilisation de raise à la fin (erreur si au début du fonction)


# if __name__ == '__main__' :
#     print(say(135995))
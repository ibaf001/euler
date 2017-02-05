
from itertools import combinations,permutations
num = ['1','2','3','4','5','6','7','8','9']

def isPandigital(x):
    x = list(x)
    x.sort()
    return x == num


def mknum(lst):
    total =''
    for n in lst:
        total += n 
    return total

def multiplicatiers(lst):
    res = []
    for n in num:
        if n not in lst:
            res.append(n)
    return res        

visited = set()
somme = 0
for x in (3,4):
    muliplicands = list(permutations(num,x))
    for multiplicand in muliplicands:
        for n in range(1,5-x+1):
            mults = list(permutations(multiplicatiers(multiplicand),n))
            for mult in mults:
                a = mknum(multiplicand)
                b = mknum(mult)
                c = int(a)*int(b)
                if isPandigital(a+b+str(c)):
                    if c not in visited:
                        visited.add(c)
                        somme += (c)
    

print('somme = {}'.format(somme))
print('Done')
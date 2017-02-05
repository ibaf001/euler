from time import time
from math import  factorial

def problem52():
    def same_digit(a,b):
        a = str(a)
        b = str(b)
        if len(a) != len(b):
            return False
        c = list(a)
        d = list(b)
        c.sort()
        d.sort()
        return c == d
    n = 10000
    
    while True:
        if same_digit(n, 2*n):
            if same_digit(n, 3*n):
                if same_digit(n, 4*n):
                    if same_digit(n, 5*n):
                        if same_digit(n, 6*n):
                            break
        
        n+= 1
    return n
def problem53():
    def comb(n,r):
        return factorial(n)//(factorial(r)*factorial(n-r))
    count = 0
    for n in range(1,101):
        for r in range(n+1):
            if comb(n,r) > 1000000:
                count += 1
        
    return count

def problem57():
    expansion = 1
    num = 3
    den = 2
    count = 0
    while expansion < 1000:
        den,num = num + den, 2*den +num 
        if len(str(num)) > len(str(den)):
            count += 1 
        expansion += 1
    return count

def problem62():
    d = {}
    def mkey(num):
        """make key for dictionary based on input number"""
        a = list(str(num))
        a.sort()
        return ''.join(a)

    for n in range(1,10000):
        v = n**3
        key = mkey(v)
        if key not in d:
            d[key] =[v]
        else:
            d[key].append(v)
            if len(d[key]) == 5:
                return (d[key])[0]
            

def problem92():

    for n in range(10000000):
        pass
    
def squareDigit(n):
    total = 0
    while n > 10:
        total += (n % 10)**2
        n //= 10
    total += n**2
    return total    
def main():
    start = time()
    #print(list(itertools.permutations([1,2,3],3)))
    #print(problem92())
    
    print(squareDigit(85))
    print(squareDigit(89))
    print(squareDigit(145))
    print(str((time() - start)*1000)+' msec')
if __name__ == '__main__':
    main()
    
    
    
    
    
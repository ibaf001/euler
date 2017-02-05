from time import time
from mes_utils import *
import math
import sys
import itertools
def problem1():
    somme = 0
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            somme += n
    return somme

def problem2():
    d = {}
    somme = 0
    
    for n in range(1,40):
        x = fibonacci(n, d)
        if x < 4000000:
            if x % 2 == 0 :
                somme += x 
    return somme

def problem3():
    s = set()
    p = 2
    n = 600851475143
    while n != 1:
        if n % p == 0:
            n = n // p
            s.add(p)

        else:
            p += 1
    print('Done.')
    return max(s)
def problem4():
    largest = 0
    for i in range(100,1000):
        for j in range(100, 1000):
            n = i * j 
            if palindromic(str(n)):
                if largest < n:
                    largest = n                    
    return largest

def problem5():
    r = 0
    a = 1
    for b in range(2,21):
        r = lcm(a,b)
        a= r
    return r

def problem6():
    def sumsquare(n):
        """sum of square of first n natural numbers
        e.g n = 10, 1**2 +2**2 +3**2+ ..+ 10**2 """
        return n**3/3 + n**2/2 + n/6
    def sum_first_n(n):
        """sum of first n natural numbers
        e.g n = 10, 1+2+3+ ..+ 10 """
        return (n**2 + n)/2
    return (sum_first_n(100))**2 - sumsquare(100)
    

def problem7():
    return primes1(200000)[10000]
def problem8():
    def prod(num):
        p = 1
        for x in num:
            p = p * int(x)
        return p
    largest = 0
    f = open('dossier/quest8.txt')
    n = ''
    for line in f:
        n += line.rstrip()
    idx = 0
    while idx < len(n):
        x = prod(n[idx:idx+13])
        if largest < x:
            largest = x 
        idx = idx + 1
    return largest

def problem9():
    for a in range(400):
        for b in range(a,400):
            for c in range(b,int((a**2+b**2)**0.5) + 1):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    return a*b*c
def problem10():
    return sum(primes2(2000000))


def problem12():
    
    ltriangle= 0
    start = 1
    def sum_first_n(n):
        """sum of first n natural numbers
        e.g n = 10, 1+2+3+ ..+ 10 """
        return (n**2 + n)//2
    tn = 0
    while ltriangle <= 500:
        tn = sum_first_n(start) #triangle number
        
        ltriangle = len(factors(tn))
        start += 1
    return tn

def problem14():
    d = {}
    def f(n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3*n + 1
    def flen(n,l=0):
        if n in d:
            return l + d[n]
        if n == 1:
            return 1 +l
        n = f(n)
        l += 1
        return flen(n,l)
    largest = 0
    num = 0
    #return flen(26)
    for x in range(13,1000000):
        l = flen(x)
        if x not in d:
            d[x] = l
        if largest < l:
            largest = l
            num = x 
    # the answer for the problem is the value of num
    return (num,largest)

def problem16():
    num = str(2**1000)
    somme = 0
    for x in num:
        somme += int(x)
    return somme

def problem20():
    num = str(math.factorial(100))
    somme = 0
    for x in num:
        somme += int(x)
    return somme

def problem21():
    d = {}
    total = 0
    def divsum(num):
        #res = []
        somme = 0
        for x in range(1, num//2 + 1):
            if num % x == 0:
                somme += x

        return somme
    for n in range(1,10000):
        am = divsum(n)
        if n not in d:
            if n == divsum(am) and n != am:
                print(n,am)
                total += (n+am)
                d[n] = am
                d[am] = n
    return total

def problem24():
    a = list(itertools.permutations([0,1, 2,3,4,5,6,7,8,9]))
    return ''.join(str(x) for x in a[1000000-1])
def problem25():
    for n in range(12,10000):
        if len(str(fibonacci(n))) == 1000:
            return n
    return -1



def problem29():
    d ={}
    for a in range(2,101):
        for b in range(2,101):
            n = a**b
            if n not in d:
                d[n] = n
    return len(d)

def problem30():
    def sdigit5(num):
        """Return sum of digit power 5"""
        p = 5
        somme = 0
        for x in str(num):
            somme += (int(x)**p)
        return somme
    total = 0
    count = 0
    for n in range(10,300000):
        if sdigit5(n) == n:
            total += n

    return total
            
        

def problem31():
    target = 200
    coins = [1,2,5,10,20,50,100,200]
    ways =[0]* 201
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i],target+1):
            ways[j] += ways[j - coins[i]]
    
    return ways[target]


def problem34():
    def cnum(num):
        somme = 0
        for x in str(num):
            somme += math.factorial(int(x))
        return num == somme
    total = 0
    for n in range(3,100000):
        if cnum(n):
            total += n
    return total

def problem35():
    d = primes2(1000000)
    dico  = {}
    for x in d:
        dico[x] = 1
    def isCircular(num):
        """Return true if number num is prime for every rotation"""
        n = len(str(num))
        exp = n -1
        while n > 1:
            r = num % 10
            q = num // 10
            num =r * (10)**(exp) + q
            if num not in dico:
                return False
            n -= 1
        return True
    count = 0
    for x in d:
        if isCircular(x):
            count += 1
    return count
            
        
        

def problem36():
    somme = 0
    for n in range (1,1000000):
        b = dec_to_bin(n)
        if palindromic(str(n)) and palindromic(str(b)):
            #print(n)
            somme += n
    return somme

    

def problem39():
    d = {}
    for a in range(1,1000):
        for b in range(a,1000):
            c = (a**2 + b **2)**0.5
            p = (a+b+c)
            if p <= 1000:
                if p not in d:
                    d[p] = 1
                else:
                    d[p] += 1
    largest = 0
    res = 0
    for k, v in d.items():

        if v > largest:
            largest = v
            res = k
    return res,largest

def problem40():
    n = 22
    d =['0123456789101112131415161718192021']
    while n < 1000000:
        #num += str(n)
        d.append(str(n))
        n += 1
    d = ''.join(d)
    #d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000    
    return int(d[1]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])

def problem42():
    d ={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,
        "V":22,"W":23,"X":24,"Y":25,"Z":26}
    f = open('dossier/quest42.txt')
    line = f.readline()
    words = line.split(",")
    count = 0
    def getnumber(word):
        total = 0
        for _ in word:
            total += d[_]
        return total
    def isTriangle(tn):
        return (1 + (1 + 8*tn)**0.5).is_integer()
    for w in words:
        if isTriangle(getnumber(w[1:-1])):
            count += 1

    return count
        
    
def problem44():
    res = sys.maxsize
    def absv(n):
        if n < 0:
            return -n
        return n
    
    def p(n):
        return int(n *(3*n -1)/2)
    d = {}
    l = []
    for n in range(1,2500):
        x = p(n)
        d[x] = x
        l.append(x)
    
    for a in l:
        for b in l:
            if a != b:
                if (a+b) in d and absv(a-b) in d:
                    if res > absv(a-b):
                        res = absv(a-b)
        
    return res

def problem45():
    def t(n):
        return n*(n+1) // 2
    
    def p(n):
        return n*(3*n-1)//2
    def h(n):
        return n*(2*n-1)
    
    dt = {}
    dp = {}
    dh = {}
    res = []
    for n in range(1,100000):
        xt = t(n)
        xp = p(n)
        xh = h(n)
        dt[xt] = n
        dp[xp] = n
        dh[xh] = n
    
    for k in dt:
        if k in dp and k in dh:
            res.append(k)
            if len(res) == 3:
                return res[2]
    
def problem47():
    n = 10
    def primes_factors(n):
        primfac = set()
        d = 2
        while d*d <= n:
            while (n % d) == 0:
                primfac.add(d)  # supposing you want multiple factors repeated
                n //= d
            d += 1
        if n > 1:
            primfac.add(n)
        return primfac
    while True:
        if len(primes_factors(n)) == 4 and len(primes_factors(n+1)) == 4 and len(primes_factors(n+2)) == 4 and len(primes_factors(n+3)) == 4:
            return n 
        n +=1          
def problem48():
    somme = 0
    for n in range(1,1001):
        somme += (n**n)
    t = str(somme)
    return t[-10:]

def problem50():
    primes = primes2(1000000)
    return 'Done ibolas'
          

def main():
    start = time()
    #print(list(itertools.permutations([1,2,3],3)))
    print(problem42())
    print(str((time() - start)*1000)+' msec')
    
if __name__ == '__main__':
    main()
        
    
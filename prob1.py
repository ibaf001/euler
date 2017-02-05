from itertools import permutations
from itertools import combinations
from time import time
from astropy.modeling.utils import comb
#print(list(permutations([1,2,3])))


def problem41():
    from random import randint
    
    def buildnum(lst):
        num = 0
        for x in lst:
            num = (num*10) + x
        return num
    def isPrime(n, k = 5):
        """probabilisticly check if number is prime """
        for i in range(k):
            a = randint(1,n-1)
            val = pow(a,n-1,n)
            if val != 1 :
                return False
        return True
    largest_n_digit = 0
    limit = 7
    while limit > 3:
        lst =list(range(1,limit+1))
        perms = list(permutations(lst))
        for n in perms:
            if n[-1] not in [0,2,4,5,6,8]:
                x = buildnum(n)
                if isPrime(x):
                    
                    if largest_n_digit < x:
                        largest_n_digit = x
        if largest_n_digit != 0:
            return largest_n_digit
        limit -= 3
    
    
def problem37():
    from random import randint
    def isPrime(n, k = 5):
        """probabilisticly check if number is prime """
        if n == 1:
            return False
        for i in range(k):
            a = randint(1,n-1)
            val = pow(a,n-1,n)
            if val != 1 :
                return False
        return True
    def ditruncable(num):
        if not isPrime(num):
            return False
        
        a = str(num)
        #b = str(num)
        n = len(a)
        for x in range(1,n):
            if not isPrime(int(a[:-x])) or not isPrime(int(a[x:])) :
                return False
        return True
    count = 0
    n = 11
    somme = 0
    while count < 11:
        if ditruncable(n):
            somme += n
            count += 1 
        n += 2
    
    return somme
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def problem69():
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    def phi(n):
        result  = n
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                while n % p == 0:
                    n /= p 
                result *= (1 - (1 / p) )
        if n > 1:
            result *= (1 - (1 / n) )
        return int(result)
            
    largest = 0
    rep = 0
    for n in range(1,11):
        x =  n/phi(n)
        if largest < x:
            largest = x
            rep = n


    return rep

def problem71():
    lst = []
    limit = 8
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    for d in range(2,(limit**0.5)+1):
        for n in range(d-1,0,-1):
            pass
def main():
    start = time()
  
    print(len(primes(100000)))
    print('{} msec elapsed'.format((time()-start)*1000))

if __name__ == '__main__':
    main()
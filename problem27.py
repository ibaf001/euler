import math
from time import time 
start = time()
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

d ={}
pr = primes(3000)
for p in pr:
    d[p] = p
bs = primes(1000)
longest = 0
xa = 0
xb = 0
for a in range(-999,1000):
    for b in bs:
        x = 0
        n = 1
        while True:

            x = n**2 + a*n + b
            if x not in d:
                if longest < n:
                    longest = n
                    xa = a
                    xb = b
                break
            
            n += 1
    
    
  
print(xa*xb)
end = time()
print('elapsed {} msec'.format((end-start)*1000))

    
    
    
    
    
    
    
    
    
    
    
    
    

        

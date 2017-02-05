from time import time
from itertools import permutations 
start = time()
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

pr = primes(10000)
d = {}
count = 0
break2= False
for p in pr:
    d[p] = p
for n in range(1001,10000,2):
    if break2:
        break
    if n in d:
        
        nums = list(permutations(list(str(n))))
        
        for num in nums:
            a = int(''.join(num))
            if a > n and a in d :
                b = a + (a-n)
                if tuple(str(b)) in nums and b in d:
                    count += 1
                    if count == 2:
                        print(str(n)+str(a)+str(b))
                        break2 = True
                        break
                    #print(n,a,b)
                    
                
                    

end= time()

print('elapsed {} msec'.format((end-start)*1000))
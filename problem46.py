from time import time 
start = time()
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

pr = primes(1000000)
d={}
r ={}
for v in pr:
    d[v] = v
idx = 4
n = 9
flag = True
res = 0
while flag:
    found = 0
    break2 = False 
    if n > pr[idx]:
        idx += 1
    if n not in d:
        xs = pr[:idx]
        for x in xs:
            if break2:
                break
            for y in range(1,int(((n-x)/2)**0.5)+1):
                if (x,y) in r:
                    calc = r[(x,y)]
                else:
                    calc = x + 2*(y**2)
                    r[(x,y)] = calc
                
                if n == calc:
                    found = 1
                    break2 = True
                    break

                
        
        if found == 0:
            res = n
            flag = False
    n += 2
    
    
print(res)   
print('Done')
end = time() 
print('elapsed {} msec'.format((end-start)*1000))





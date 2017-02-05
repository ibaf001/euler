from time import time 
start = time()
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]
LIMIT = 1000000
pr = primes(LIMIT)
n = len(pr)
db = [0] #*(n+1)
d = {}
somme = 0
i = 0
while i < n:
#for i in range(n):
    #db[i+1] = (somme + pr[i])
    db.append(somme + pr[i])
    #d[pr[i]] = pr[i]
    somme = db[i+1]
    if somme >= LIMIT:
        i = n
    i += 1


m = len(db)
flag = True
k = 0

while flag:
    d[pr[k]] = pr[k]
    k += 1

    if len(d) >= len(pr):
        break
    
res = 0
longest = 0
rx,ry = 0,0
for i in range(m):
    for j in range(i+1,m):
        dist = j - i
        num = db[j] - db[i]
        if num >= LIMIT:
            break
        else:
            if num in d:

                if longest < dist:
                    longest = dist
                    rx = i 
                    ry = j
                    res = num

print(res,(rx,ry))
print('Done.')
end = time()
print('elapsed {} msec'.format((end-start)*1000))

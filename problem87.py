from time import time

start = time()
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]
a = primes(7072)
b = primes(369)
c = primes(86)

aa= [x**2 for x in a]
bb= [x**3 for x in b]
cc= [x**4 for x in c]

count = 0
visited = set()
d = {}
for x in range(len(a)):
    for y in range(len(b)):
        if aa[x] + bb[y] >= 50000000:
            break
        else:
            for z in range(len(c)) :
                num = aa[x] + bb[y] + cc[z]
                if num < 50000000:
                    if num not in d:
                        count += 1
                        d[num] = num
                else:
                    break

print(count)

end= time()
print('elapsed {} msec'.format((end-start)*1000))
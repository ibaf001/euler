from time import time

start = time()
from itertools import permutations 
def divprop(d):
    primes =[2,3,5,7,11,13,17]
    idx = 0
    for n in range(1,8):
        if int(''.join(d[n:n+3])) % primes[idx] != 0:
            #print(d[n:n+3],n,primes[idx])
            return False
        idx += 1
    return True

#print(divprop(['1','4','0','6','3','5','7','2','8','9']))


d = list(permutations(['0','1','2','3','4','5','6','7','8','9']))
somme = 0

for num in d:
    if num[0] != '0':
        if divprop(num):
            
            somme += int(''.join(num))

print(somme)
end = time()
print('elapsed time {} msec'.format((end-start)*1000))

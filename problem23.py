import math
from time import time
start = time()
def dvs(n):
    somme = 0
    
    for x in range(1,int(math.sqrt(n))+ 1):
        if n % x == 0:
            somme += x
            if x * x != n and n//x != n:
                somme += (n//x)
    
    return somme
limit = 28124 
           
abn = [x for x in range(1,limit) if dvs(x) > x]
ln = len(abn)
somme = 0


visited = set()
for a in abn:
    for b in abn:
        if a+b >= limit:
            break
        visited.add(a+b)

for x in range(1,limit):
    if x not in visited:
        somme += x


print(somme)
end = time()

print('elapsed {} mec'.format((end - start)*1000))
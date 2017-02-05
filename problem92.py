from time import time 
start = time()
sqr = [x**2 for x in range(10)]

def convert(num):

    res = 0
    while num > 0:
        res += sqr[num % 10]
        num = num // 10 
   
    return res
d = {1: {}, 89: {}}
def chaine(n, s):
    if n in d[89]:
        d[89].update(s)
        return 89
    if n in d[1]:
        d[1].update(s)
        return 1

    if n == 1:
        d[1].update(s)
        return 1
    if n == 89:
        d[89].update(s)
        return 89
    x = convert(n)
    s[n] =  x
    return chaine(x,s)

count = 0
for n in range(2,10000000):
    s = {}
    if chaine(n,s) == 89:
        count += 1
        
print(count)
end = time()

print('elapsed {} msec'.format((end-start)*1000))

from time import time 
import sys
start = time()

def isWhole(num):
    return num % 1 == 0
limit = 1000
sqr = [x**2 for x in range(0,limit)]
w, h = limit, limit
m = [[sys.maxsize for x in range(w)] for y in range(h)] 


largest = 0
for i in range(1,limit):
    for j in range(1,limit):
        d = (sqr[i] - 1)/sqr[j]
        if isWhole(d):
            m[i][j] = d








end = time()

print('elapsed {} msec'.format((end-start)*1000))
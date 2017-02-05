from time import time
d = {}
def isPalindromic(num):
    return str(num)[::-1] == str(num)

def revAdd(num,x = 0):
    if x == 50:
        return -1
    if num in d:
        return x + d[num]
    if x > 0 and isPalindromic(num):
        return x 
    x += 1
    num = num + int(str(num)[::-1])
    return revAdd(num,x)
start = time()
count = 0
for n in range(1,10000):
    x = revAdd(n)
    if x == -1:
        count += 1 
    else:
        d[n] = x

print('count = '+ str(count))
print(len(d))
end = time()  

print('elapsed {} msec'.format((end-start)*1000))








    
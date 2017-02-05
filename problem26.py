from time import time 
start = time()
def repeatLength(d):
    map = {}
    p = len(str(d))
    
    x = 10**p
    for i in range(d):
        qt = x // d
        if qt in map:
            if (x % d) in map[qt]:
                return i - map[qt][x%d]
        
        reste = x % d
        map[qt] = {reste : i}
        if reste == 0:
            return -1
        x = (reste)*(10**p)
    print(map)
    return -1

largest = 0
num = 0
for n in range(2,1000):
    a = repeatLength(n)

    if a != -1 :
        if largest < a:
            num = n
            largest = a
          
print(num)
end=time() 

print('elapsed {} msec'.format((end-start)*1000))
        
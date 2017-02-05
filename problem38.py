from time import time
start = time()
def isPandigital(n):
    n = list(n)
    n.sort()
    return n == ['1','2','3','4','5','6','7','8','9']
largest = 0
for num in range(1,10001):
    x = ''

    for n in range(1,10):
        x += str(num * n)
        if len(x) > 9:
            break
        elif len(x) == 9:

            if isPandigital(x):
                if largest < int(x):
                    largest = int(x)

print('the number is {}'.format(largest))
end = time()
print('done. it took {} msec'.format((end-start)*1000))



            
        
        



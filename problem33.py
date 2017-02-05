from time import time
start = time()
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def non_trivial(a,b):
#     if a % 10 == 0 and b % 10 == 0:
#         return -1
    a1 = a // 10
    a2 = a % 10
    b1 = b //10
    b2 = b % 10
    if a1 / b1 == a /b and a2 == b2:
        return (a1,b1)
    elif a1/b2 == a/b and a2 == b1:
        return (a1,b2)
    elif a2/b1 ==  a/b and a1 == b2:
        return (a2, b1)
    elif a2 /b2 ==  a/b and a1 == b1:
        return (a2,b2)
    else:
        return -1
    
numprod = 1
denprod = 1
for num in range(10,100):
    for den in range(num+1,100):
        if den % 10 != 0:
            x = non_trivial(num, den)
            if x != -1:
                numprod *= x[0]
                denprod *= x[1]

            
print(denprod / gcd(numprod,denprod))
end = time()
print("elapsed time {} msec".format((end-start)*1000))

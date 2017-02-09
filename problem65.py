def nd(a,b,c):
    '''Return num and den for a + 1/b '''
    return (b+a*c,c)

def seq(n):
    k = 0
    a,b=1,  (n//3)*2 if n % 3 == 0 else 1 

    for x in range(n-1,1,-1):
        if x % 3 == 0:
            k = (x//3)*2
        else:
            k = 1
        b,a = nd(k,a,b)
        

    return nd(2,a,b)

def sumdigit(num):
    total = 0
    while num > 0:
        total += (num % 10)
        num = num // 10 
    return total 

print(sumdigit(seq(100)[0]))
    





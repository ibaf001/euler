from time import time
def prob1():
    total = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total

def prob16():
    num = str(2 ** 1000)
    total = 0
    for n in num:
        total += int(n)
    return total
    
def prob2():
    a,b,total = 1, 2,0
    while b < 4000000:
        if b % 2 == 0:
            total += b
        a,b = b,b + a
    return total

def prob3():
    liste = primesfactors(600851475143)
    return max(liste)


def prob4():
    res = 0
    for a in range(100,1000):
        for b in range(100,1000):
            val = a * b
            if isPalindromic(val):
                if val > res:
                    res = val
    return res




def prob6():
    return (sum_first_n(100))**2 - sumsquare(100)

def sumsquare(n):
    """sum of square of first n natural numbers
    e.g n = 10, 1**2 +2**2 +3**2+ ..+ 10**2 """
    return n**3/3 + n**2/2 + n/6

def sum_first_n(n):
    """sum of first n natural numbers
    e.g n = 10, 1+2+3+ ..+ 10 """
    return (n**2 + n)/2
        
                
def primesfactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac



def isPalindromic(n):
    n = str(n)
    return n == n[::-1]

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm

def main():
    start = time()
  
    end = time()
    print("elapsed time is {} seconds".format((end- start)))

if __name__ == '__main__':
    main()
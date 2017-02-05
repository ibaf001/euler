
import functools
# a = itertools.permutations([1, 2, 3])
# b = list(itertools.combinations([0,1,2,3,4,5,6,7,8,9],7))
# c = itertools.combinations()
# n = 0
# for n in range(2,10):
#     lst1 = list(itertools.combinations([0,1,2,3,4,5,6,7,8,9],n))
def lcm(a, b):
    """Return the least common multiple of two number"""
    if a > b:
        a,b = b, a
    
    for x in range(b, a*b+1,b):
        if x % a == 0:
            return x 
def palindromic(num):
    if len(num) <= 1:
        return True
    if num[0] != num[-1]:
        return False
    return palindromic(num[1:-1])


def fibonacci(n, d={}):
    if n in d:
        return d[n]
    if n == 1 or n == 2:
        return 1
    total= fibonacci(n-1,d) + fibonacci(n-2,d)
    d[n] = total
    return total


def primes1(n):
    listPrimes = []
    
    for x in range(2,n+1):
        isPrime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                isPrime = False
                break
        if isPrime:
            listPrimes.append(x)
    return listPrimes

def primes2(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def isPandigital(num):
    n = len(num)
    d = {}
    lst =list(range(1,n+1))
    for x in num:
        if int(x) not in lst:
            return False
        else:
            if x not in d:
                d[x] = 1
            else:
                return False
    return len(d) == n

def isPandigital9(num):
    n = 9
    d = {}
    lst =list(range(1,n+1))
    for x in num:
        if int(x) not in lst:
            return False
        else:
            if x not in d:
                d[x] = 1
            else:
                return False
    return len(d) == n

def factors(n):    
    return set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
#print(isPandigital9('239451678'))      
#print(len(primes2(10000000)))
#print((primes1(200000))[5])
def dec_to_bin(x):
    return int(bin(x)[2:])

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def same_digit(a,b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    c = list(a)
    d = list(b)
    c.sort()
    d.sort()
    return c == d

def mkey(num):
    """make key for dictionary based on input number"""
    a = list(str(num))
    a.sort()
    return ''.join(a)
#print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#print(list(itertools.permutations([0,1, 2])))
def sdigit5(num):
    """Return sum of digit power 5"""
    p = 5
    somme = 0
    for x in str(num):
        somme += (int(x)**p)
    return somme
 
def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
def primes_factors(n):
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

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]










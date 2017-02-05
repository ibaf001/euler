def factors(n):
    ''' Return primes factors'''
    primfac = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.add(n)
    return primfac

n = 2
largest = 0
res = 0
while n <= 1000000:
    f = factors(n)
    prod = 1
    for p in f:
        prod = prod*(1-1/p)
    if largest < 1/prod:
        largest = 1/prod
        res = n
        
    n += 2

print(res)
print('Done')
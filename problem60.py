d = {}
t = {}


def v(n):
    if n in d:
        return d[n]
    if n == 1:
        return 5
    elif n == 2:
        return 65
    elif n == 3:
        return 901
    total = 15*v(n-1) - 15*v(n-2) + v(n-3)
    d[n] = total
    return total

def w(n):
    if n in t:
        return t[n]
    if n == 1:
        return 16
    elif n == 2:
        return 240
    elif n == 3:
        return 3360
    total = 15*w(n-1) - 15*w(n-2) + w(n-3)
    t[n] = total
    return total

n = 1 
somme = 0
p1 = 0 
p2 = 0
while p1 < 1000000000 and p2 < 1000000000:
    a = v(n)  #2 sides
    b = a + 1
    p1 = 2*a + b 
    x = w(n)
    y = x + 1 #2sides
    p2 = 2*y +x
    
    if p1 < 1000000000:
        somme += p1 
    if p2 < 1000000000:
        somme += p2
    
    n += 1

print(somme)

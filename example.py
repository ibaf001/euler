from math import factorial
d = {}
def sumfact(num):
#     if num in d:
#         return d[num]
    f = [1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    total = 0
    while num >= 10:
        total += f[num % 10]
        num //= 10
    total += f[num]
    #d[x] = total
    return total


print(sumfact(69))



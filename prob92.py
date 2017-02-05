from nbformat.validator import isvalid
def isPandigital(num):
    if len(num) < 9 :
        return False
    a = list(num)
    a.sort()
    return a == ['1','2','3','4','5','6','7','8','9']

def isValid(num):
    a = str(num)
    if '0' in a:
        return False
    b = set(str(a))
    return len(a) == len(b)

limit =10000 # 31500
#x = [n for n in range(1,limit) if isValid(n)]

for a in range(1,limit+1 ):
    for b in range(a,limit+1):
        pass

print(isPandigital('243576981'))
print(isPandigital('24356981'))


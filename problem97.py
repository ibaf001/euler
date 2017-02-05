a = 28433*(2**7830457)+1



res = ''
for n in range(10):
    res = str(a % 10)+res
    a = a // 10
    
print(res)
print('done')
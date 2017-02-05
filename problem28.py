def spiral(n):
    return 4*(2*n + 1)**2 - 12*n


total = 1
for k in range(1,501):
    total += (spiral(k))
print(total)
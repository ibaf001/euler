def getSum(num):
    total = 0 
    for n in num:
        total += int(n)
    return total

f = open('problems/prob13.txt')
total = 0
for line in f:
    line = line.strip().split()
    total += getSum(line)

print(str(total)[:10])
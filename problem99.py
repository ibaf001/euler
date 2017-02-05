from math import log10

f = open('dossier/prob99.txt')

n = 1
a = 1
res = 0
for line in f:
    line = line.strip().split(',')
    num = int(line[1]) * log10(int(line[0]))
    if a < num:
        a = num
        res = n

    n += 1 
        
        
print(res)
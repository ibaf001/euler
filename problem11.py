f = open('problems/prob11.txt')

for line in f:
    line = line.strip().split()
    print(line)
from time import time
start = time()
size = 20
tab =  [[0 for x in range(size+1)] for y in range(size+1)] 
for i in range(size+1):
    tab[i][size] = 1
    tab[size][i] = 1
    
for x in range(size-1,-1,-1):
    for y in range(size-1,-1,-1):
        tab[x][y] = tab[x+1][y] + tab[x][y+1]
        
        
print(tab[0][0])
end = (time() -start)*1000
print('elapsed {} msec'.format(end))





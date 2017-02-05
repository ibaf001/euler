
total = 200
sums = [0]* (total + 1)
sums[0] = 1
for j in [1,2,5,10,20,50,100,200]:
    for  s in range(1,total+1):
        if j <= s:
            sums[s] += sums[s-j]

    

print(sums[total])
from _ast import Num
def digitalSum(num):
    total = 0
    for n in str(num):
        total += int(n)
    return total


largest = 0
for a in range(1,100):
    for b in range(1,100):
        num = digitalSum(a** b)

        if largest < num:
            largest = num

print(largest)


        
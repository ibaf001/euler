count = 0
for a in range(1,101):
    for b in range(1,101):
        if len(str(a**b)) == b:
            count += 1
print(count)
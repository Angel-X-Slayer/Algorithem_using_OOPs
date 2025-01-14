stock = [3, 1, 4, 8, 7, 2, 5]
prof = 0
for i in range(1, len(stock)):
    if stock[i] > stock[i-1]:
        prof += stock[i]-stock[i-1]
print(prof)

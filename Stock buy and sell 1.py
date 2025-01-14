stock = [3, 1, 4, 8, 7, 2, 5]
helper = [0]*len(stock)
# print(helper)
maxi = max(stock)
for i in range(len(stock)):
    if stock[i] < maxi:
        maxi = stock[i]
    helper[i] = maxi
# print(helper)
maxi = 0
for i in range(len(helper)):
    maxi = max(maxi, stock[i]-helper[i])
print(maxi)

def diff(n, m):
    div = 0
    non_div = 0
    for i in range(m+1):
        if i % n == 0:
            div += i
        else:
            non_div += i
    print(abs(div-non_div))


n = int(input("enter the value of n :"))
m = int(input("enter the value of m : "))
diff(n, m)

def solution(num1, num2):
    op = 0
    carry = 0
    arr1 = []
    arr2 = []
    num1 = str(num1)
    num1 = "".join(reversed(num1))
    num2 = str(num2)
    num2 = "".join(reversed(num2))
    for i in num1:
        arr1.append(i)
    for i in num2:
        arr2.append(i)
    if len(arr1) >= len(arr2):
        for i in range(len(arr1)):
            if i <= len(arr2)-1:
                if int(arr1[i])+int(arr2[i])+carry > 9:
                    op += 1
                    carry = 1
                else:
                    carry = 0
                    op += 0
            else:
                if int(arr1[i])+carry > 9:
                    op += 1
                    carry = 1
                else:
                    op += 0
                    carry = 0
    elif len(arr2) > len(arr1):
        for i in range(len(arr2)):
            if i <= len(arr1)-1:
                if int(arr2[i])+int(arr1[i])+carry > 9:
                    op += 1
                    carry = 1
                else:
                    carry = 0
                    op += 0
            else:
                if int(arr2[i])+carry > 9:
                    op += 1
                    carry = 1
                else:
                    op += 0
                    carry = 0

    print(op)


solution(449, 459636)

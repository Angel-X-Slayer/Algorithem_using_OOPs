
def solution(arr, target):
    arr.sort()
    if arr[0]+arr[1] >= target:
        print(0)
    else:
        print(arr[0]*arr[1])


# arr = [5, 2, 4, 3, 9, 7, 1]
arr = [9, 8, 3, -7, 3, 9]
solution(arr, 4)

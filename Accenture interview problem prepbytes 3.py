def solution(arr):
    odd = []
    even = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    sorted_odd = sorted(odd, reverse=True)
    sorted_even = sorted(even, reverse=True)
    print(sorted_odd[1]+sorted_even[1])


arr = [3, 2, 1, 7, 5, 4]
# arr = [1, 8, 0, 2, 3, 5, 6]
solution(arr)

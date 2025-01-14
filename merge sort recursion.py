def merge_sort(arr):
    if len(arr) > 1:
        left_half = arr[:len(arr)//2]
        right_half = arr[len(arr)//2:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        return (arr)
    else:
        return (-1)


arr = [2, 1, 4, 3, 7, 5, 6, 8, 1, 0, 9, 1, 2]
sorted_arr = merge_sort(arr)
print(sorted_arr)

def bubble_sort(arr1):
    n = len(arr1)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]


arr = [64, 34, 25, 12, 22, 11, 90]
print(sorted(arr, reverse=True))

bubble_sort(arr)

print(arr)

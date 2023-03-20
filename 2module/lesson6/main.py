# two pointers - метод двух указателей
# сложность алгоритма O(N)


arr1 = [1, 2, 6, 100, 500, 18888]
arr2 = [3, 4, 10, 12]

# i -> arr1
# j -> arr2
i = j = 0
massive = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        massive.append(arr1[i])
        i += 1
    else:
        massive.append(arr2[j])
        j += 1

while i < len(arr1):
    massive.append(arr1[i])
    i += 1

while j < len(arr2):
    massive.append(arr2[j])
    j += 1


print(massive)

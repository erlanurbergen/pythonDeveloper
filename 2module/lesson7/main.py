# Merge sort - Сортировка слиянием
# O(nlog(n))

"""
12, 11, 13, 5, 6, 7
12 11 13                 5 6 7
12    11 13              5     6 7
[12]   [11, 13]          [5]   [6, 7]
[11 12 13]               [5 6 7]
[5 6 7 11 12 13]
"""

def twoPointers(arr1, arr2):
    
    i = j = 0
    massive = []

    while i < len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j] :
            massive.append(arr1[i])
            i += 1
        else :
            massive.append(arr2[j])
            j += 1

    while i < len(arr1) :
        massive.append(arr1[i])
        i += 1

    while j < len(arr2) :
        massive.append(arr2[j])
        j += 1

    return massive


def mergeSort(list1):

    if len(list1) == 1:
        return list1

    middle = len(list1) // 2
    rigth = mergeSort(list1[middle:])
    left = mergeSort(list1[:middle])
    return twoPointers(left, rigth)


arr1 = [12, 11, 13, 5, 6, 7]
print(*mergeSort(arr1))
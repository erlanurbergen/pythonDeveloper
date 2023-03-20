# bubble sort - сортировка пузырьком
# сложность алгоритма O(n*2)

arr1 = [64, 34, 25, 12, 22, 11, 90]
"""
Сортируем от меньшего к большому
1 step: 34, 25, 12, 22, 11, 64, 90 count = 5
2 step: 25, 12, 22, 11, 34, 64, 90 count = 9
3 step: 12, 22, 11, 25, 34, 64, 90 count = count 12
4 step: 12, 11, 22, 25, 34, 64, 90 count = count 13
5 step: 11, 12, 22, 25, 34, 64, 90 count = count 14
"""

count = 0
for item in range(len(arr1) - 1):
    for i in range(len(arr1) - 1 - item):
        print(f"equals {arr1[i]} with {arr1[i + 1]}")
        if arr1[i] < arr1[i+1]:
            count += 1
            arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
    # print(f"{item} step: {arr1}")
print(arr1)
print(count)

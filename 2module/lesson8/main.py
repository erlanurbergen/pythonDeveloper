# Quick sort - быстрая сортировка
"""
Quicksort — это алгоритм сортировки сравнением с посредственной производительностью.
Быстрая сортировка использует метод разбиения и может выполняться в лучшем случае и в среднем за O( n log ( n )).
Однако он может выполняться при O( n 2 ) в худшем случае
"""

"""
100, 8, 1, 15, 500, -9, 600
                                15
            8 1 -9                              100 500 600
               1
            -9    8
        [-9] + [1] + [8]  + [15] +  [100 500 600]  
"""

def quickSort(l):

    if len(l) <= 1:
        return l

    element = l[len(l) // 2]
    left = [item for item in l if item < element]  # BigO
    right = [item for item in l if item > element]  # BigO
    center = [item for item in l if item == element]
    return quickSort(left) + center + quickSort(right)


print(quickSort([100, 8, 1, 15, 500, -9, 600]))
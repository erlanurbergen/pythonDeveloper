# Binary search
# O(logN)
import time

# 1 -9 6 8 10 55 222 660
# 222

def binarySearch(list1, element):
    start = 0
    end = len(list1) - 1
    # 1 -9 6 8 10 55 222 660
    # -9
    check = False
    while start <= end and not check:
        middle = (start + end) // 2
        item = list1[middle]
        if item == element:
            check = True
        if item > element:
            end = middle - 1
        else:
            start = middle + 1
    return check

print(binarySearch([1, -9, 6, 8, 10, 55, 222, 660], -99))
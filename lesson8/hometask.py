"""
Create a function that takes a list and finds the integer which appears an odd number of times.
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10
"""
# def find_odd(a):
#     # 1 option
#     for value in a:
#         if a.count(value) % 2 != 0:
#             print(value)
#             break
#     # 2 option
#     # return [item for item in a if a.count(item) % 2 != 0]
#
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))

"""
Create a function that takes a list of non-negative integers and strings 
and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
"""

# def filter_list(a):
#     b = []
#     for i in a:
#         if type(i) == int:
#             b.append(i)
#     return b
#
# print(filter_list([1, 2, "a", "b"]))


"""
Create a function that takes three parameters where:

x is the start of the range (inclusive).
y is the end of the range (inclusive).
n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible 
by the third parameter n. Return an empty list if 
there are no numbers that are divisible by n.

list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []

"""

# def list_operation(a, b, c):
#     list1 = []
#     for i in range(a, b):
#         if i % c == 0:
#             list1.append(i)
#     return list1
#
# print(list_operation(1, 10, 3))

"""
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

# def high_and_low(numbers):
#     a = numbers.split(" ")
#     c = []
#     for i in a:
#         c.append(int(i))
#     # b = list(map(int, numbers.split()))
#     maxNumber = max(c)
#     mixNumber = min(c)
#     return str(maxNumber) + " " + str(mixNumber)
#
# print(high_and_low("1 2 3 4 5"))


"""
Ben has a very simple idea to make some profit: 
he buys something and sells it again. Of course, 
this wouldn't give him any profit at all if he was simply to buy and sell 
it at the same price. 
Instead, he's going to buy it for the lowest possible price and sell it at the highest.
Task
Write a function that returns both the minimum and maximum number of the given list/array.


"""
def min_max(lst):
    b = [min(lst), max(lst)]
    return b

"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), 
value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     if operator == '-':
#         return value1 - value2
#     if operator == '*':
#         return value1 * value2
#     if operator == '/':
#         return value1 / value2


"""
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int index1 = 0;
        int index2 = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target){
                    index1 = i;
                    index2 = j;
                }
            }
        }
        return new int[]{index1, index2};
    }
}

"""

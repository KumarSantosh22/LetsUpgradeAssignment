# Answer 1
# T(n) = O(n)


# Answer 2
# a)X will be a better choice for all inputs


# Answer 3
'''Input: list1 = [12, 3, 55, 6, 144]
Output: [12, 6, 144]
Input: list2 = [2, 10, 9, 37]
Output: [2, 10]
'''

num = list(map(int, input('Enter numbers : ').split()))
num = [x for x in num if x % 2 == 0]
print(num)

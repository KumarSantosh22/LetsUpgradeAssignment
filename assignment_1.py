# Answer 1:

num = list(map(int, input('Enter two number : ').split()))
a, b = num[0], num[1]
print(f'Add : {a+b} \n Sub : {a-b} \n Mul : {a*b} \n Div : {a//b}')

# Answer 2:

from math import pow
num = list(map(int, input('Enter a number with their power: ').split()))
a, n = num[0], num[1]
print(pow(a, n))

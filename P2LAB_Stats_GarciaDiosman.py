# P2LAB1
# 10/09/2022
# CTI-110 P2LAB2 - Simple statistics
# Diosman Garcia

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# creating input list
numbers = [num1, num2, num3, num4]

# calculating product of four numbers
product_all = num1*num2*num3*num4

# calculating the average
average_all = sum(numbers) / len(numbers)

# product of all numbers as integer
print(f'{product_all:.0f}', end=" ")
# average of all numbers as integer
print(f'{average_all:.0f}')
# product of all numbers as floating-point value with three digits after the decimal point
print(f'{product_all:.3f}', end=" ")
# average of all numbers as floating-point value with three digits after the decimal point
print(f'{average_all:.3f}')

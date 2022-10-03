# P2LAB1
# 10/02/2022
# CTI-110 P2LAB2 - Simple statistics
# Diosman Garcia

# floating-points
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# creating list using num1,num2,num3,num4
numbers = [num1,num2,num3,num4]
# establish a variable product_all used to store product of four numbers
product_all = 1
# iterate every number in list
for number in numbers:

    # calculating product of four numbers
    product_all = product_all * number

# calculating the average
# sum function is calculating the sum of all numbers
# len function is to find the length of the list
average_all = sum(numbers) / len(numbers)

# product of all numbers as integer
print(f'{product_all:.0f}',end=" ")
# average of all numbers as integer
print(f'{average_all:.0f}')
# product of all numbers as floating-point value with three digits after the decimal point
print(f'{product_all:.3f}',end=" ")
# average of all numbers as floating-point value with three digits after the decimal point
print(f'{average_all:.3f}')

num1 = int(input())
num2 = int(input())

if num1 <= num2:
    for i in range(num1, num2 + 1, 5,):
        print(i, end=" ")
    print()
else:
    print("Second integer can't be less than the first.")
# CTI-110 
# P3HW1 - Debugging
# Diosman Garcia
# 10/23/2022

# Ask user for grade for Module 1
mod = float(input('Enter grade for Module 1: '))
# Ask user for grade for Module 2
mod = float(input('Enter grade for Module 2: '))
# Ask user for grade for Module 3
mod = float(input('Enter grade for Module 3: '))
# Ask user for grade for Module 4
mod = float(input('Enter grade for Module 4: '))
# Ask user for grade for Module 5
mod = float(input('Enter grade for Module 5: '))
# Ask user for grade for Module 6
mod = float(input('Enter grade for Module 6: '))
# The grade list store the grades entered
grade = [mod1, mod2, mod3, mod4, mod5, mod6]
# Calculation of all Grades
# Calculate the lowest grades
low_gra = min(grade)
# Calculate the highest grades
hig_gra = max(grade)
# Calculate the sum of grades
sum_gra = sum(grade)
# Calculate the grades average
avg_gra = sum(grade)/len(grade)
# Defining minimum grade to get grade A, B, C and D
A_grade = 90
B_grade = 80
C_grade = 70
D_grade = 60
print()
#Display results
print("------------Results------------")
print("Lowest Grade:      ", f'{low_gra:.1f}')
print("Highest Grade:     ", f'{hig_gra:.1f}')
print("Sum of Grades:     ", f'{sum_gra:.1f}')
print("Average:           ", f'{avg_gra:.2f}')
print("----------------------------------------")
# if-else statements to output the grade letter corresponding to the grade inputed
if avg_gra >= A_grade:
    print("Your grade is: A")
else:
    if avg_gra >= B_grade:
        print("Your grade is: B")
    else:
        if avg_gra >= C_grade:
            print("Your grade is: C")
        else:
            if avg_gra >= D_grade:
                print("Your grade is: D")
            else:
                print("Your grade is: F")



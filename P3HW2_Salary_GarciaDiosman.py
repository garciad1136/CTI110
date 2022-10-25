# CTI-110 
# P3HW2 - Salary
# Diosman Garcia
# 10/25/2022

# This program will calculate the employee's pay after the user
# as input the following data points name, hours work, and pay rate

# START
#   DECLARE hoursWork, payRate, regHour, regPay, oveTime, oveRate, groPay as intergers
#
#   PROMPT for "Enter employee's name: "
#   GET name
#   STORE name
#   PROMPT for "Enter number of hours worked: " 
#   GET hoursWork
#   STORE hoursWork
#   PROMPT for "Enter employee's pay rate: "
#   GET payRate
#   STORE payRate
#
#   SUBTRACT hoursWork by 40
#   DIVIDE payRate by 2 then ADD by payRate
#   MUTIPLY oveTime by oveRate
#   SET regHour to 40
#   MUTIPLY payRate by regHour
#   ADD regPay by ovePay
#    
#   DISPLAY "Employee's name:    ", name
#   PRINT "Hours Worked    Pay Rate    OverTime    OverTime Pay      RegHour Pay      Gross Pay"
#   DISPLAY hoursWork, payRate, oveTime, ovePay, $regPay, $groPay
# END
    
# Identify all the variables that are interger
hoursWrok=0
payRate=0
regHour=0
regPay=0
oveTime=0
oveRate=0
groPay=0

# Ask user for their name
# Set the variable for name
name = input("Enter employee's name: ")

# Ask user for their worked hours
# Set the variable for worked hours
hoursWork = float(input("Enter number of hours worked: "))

# Ask user for their pay rate
# Set the variable for pay rate
payRate = float(input("Enter employee's pay rate: "))

# Calculation of all the data
oveTime = hoursWork - 40
oveRate = (payRate/2) + payRate
ovePay = oveTime * oveRate
regHour = 40
regPay = payRate * regHour
groPay = regPay + ovePay
    
#Display results
print("-------------------------------------")
print("Employee's name:    ", name)  
print()
print("Hours Worked    Pay Rate    OverTime    OverTime Pay      RegHour Pay      Gross Pay")
print("-----------------------------------------------------------------------------------------------")
print(hoursWork,"          ", payRate,"      ", oveTime,"       ", ovePay,"          ", f'${regPay:.1f}',"         ", f'${groPay:.1f}')

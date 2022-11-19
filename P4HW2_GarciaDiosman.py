# CTI-110 
# P4HW2 - Salary Calculator
# Diosman Garcia
# 11/18/2022

# This program will calculate the employee's pay

######PSEUDOCODE-START######
#
# START
# DECLARE num_emp, total_overT_pay, total_reg_pay, total_gro_pay as global intergers
#
# PROMPT for Enter employee's name or \"None\" to terminate: 
# STORE name
# Initiate the while true loop
# Check if "none" was enter
# if yes break and terminate the loop
# else increase employees count by 1
# PROMPT for "How many hours did " + name + " worked? " 
# STORE hours_w
# PROMPT for "What did " + name + "\' pay rate? "
# STORE pay_r
# DECLARE overT, overT_pay, reg_pay, gro_pay as employee intergers 
#
# Calculate overtime if hours_w > 40
# overT = hours_w - 40
# overT_pay = overT * pay_r * 1.5
# reg_pay = 40 * pay_r
# gro_pay = reg_pay + overT_pay
# else reg_pay = hours_w * pay_r
# Add overtime pay to total overtime pay.
# Add regular pay to total regular pay.
# Add gross pay to total gross pay.
#
# DISPLAY "\nEmployee name: " + name + "\n"
# PRINT "Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross Pay"
# DISPLAY hours_w, pay_r, overT, overT_pay, reg_pay, gro_pay
# PRINT "Total number of employees entered:"
# PRINT "Total amount payed for over time: $"
# PRINT "Total amount payed for regular hours: $"
# PRINT "Total amount payed in gross: $"
# END
#
######PSEUDOCODE-ENDS######
# Identify global variables.
num_emp = 0
total_overT_pay = 0
total_reg_pay = 0
total_gro_pay = 0

# Initiate loop until user exit
while True:
    # Ask user for their name.
    # Set the variable for name.
    name = input("Enter employee's name or \"None\" to terminate: ")
    # Check for NONE in the name variable if so break the loop no futher input.
    if name == "None":
        break
    else:   # if correct name then increase employee count by 1.
        num_emp += 1
    # Ask user for their worked hours.
    # Set the variable for worked hours.
    hours_w = float(input("How many hours did " + name + " worked? "))

    # Ask user for their pay rate.
    # Set the variable for pay rate.
    pay_r = float(input("What did " + name + "\' pay rate? "))

    # Identify variables for the employee to calculate.
    overT = 0
    overT_pay = 0
    reg_pay = 0
    gro_pay = 0

    # Identify overtime if number is > 40.
    if hours_w > 40:
        # Calculate overtime.
        overT = hours_w - 40
        # Calculate overtime pay.
        overT_pay = overT * pay_r * 1.5
        # Calculate regular pay.
        reg_pay = 40 * pay_r
        # Calculate gross pay.
        gro_pay = reg_pay + overT_pay
    # Otherwise just calculate the regular pay and gross pay.
    else:
        reg_pay = hours_w * pay_r
        gro_pay = reg_pay
    # Add overtime pay to total overtime pay.
    total_overT_pay += overT_pay
    # Add regular pay to total regular pay.
    reg_pay += total_reg_pay
    # Add gross pay to total gross pay.
    gro_pay += total_gro_pay

    #Display results
    print("\nEmployee name: " + name + "\n")  
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-----------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours_w, pay_r, overT, overT_pay, reg_pay, gro_pay))
    print()
# Complete the loop and print the employees information
print()
print("Total number of employees entered:", num_emp)
print("Total amount payed for over time: $" + '{:.2f}'.format(total_overT_pay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(total_reg_pay))
print("Total amount payed in gross: $" + '{:.2f}'.format(total_gro_pay))

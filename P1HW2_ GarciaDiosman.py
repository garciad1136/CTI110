# P1HW2
# This will be a project that adds a 6% tax on remaining balance.
# 09/15/2022
# CTI-110 P1HW2 - Travel Expense
# Diosman Garcia

print("This program clculates and displays travel expenses")
print()
# Ask user to enter their budget
user_bud = int(input('Enter Budget: '))
print()
# Ask user to enter travel destination
user_des = input('Enter your travel destination: ')
print()
# Ask user for amount they will spend on gas
user_gas = int(input('How much do you think you will spend on gas? '))
print()
# Ask user for amount they will spend on accommodation
user_acc = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
# Ask user for amount they will spend on food
user_foo = int(input('Last, how much do you need for food? '))
print()
#Add expenses
total_exp = user_gas + user_acc + user_foo
# Subtract expenses from budget
rem_bala = user_bud - total_exp * 1.0
# Add Tax
tax = rem_bala * .06
#Display results
print("------------Travel Expenses------------")
print("Location:", user_des)
print("Initial Budget:", user_bud * 1.0)
print()
print("Fuel:", user_gas * 1.0)
print("Accomodation:", user_acc * 1.0)
print("Food:", user_gas * 1.0)
print()
print("Ramining Balance:", rem_bala)
print("TAXES:", tax)
print("Total:", rem_bala + tax)

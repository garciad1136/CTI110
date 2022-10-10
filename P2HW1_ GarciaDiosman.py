# P2HW1
# This will be a project that adds a 6% tax on remaining balance.
# 10/09/2022
# CTI-110 P2HW1 - Travel
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
rem_bal = user_bud - total_exp
# Add Tax
tax = rem_bal * .06
#Display results
print("------------Travel Expenses------------")
print("Location:", f'{user_des:s}')
print("Initial Budget:", f'${user_bud:.1f}')
print("Fuel:", f'${user_gas:.1f}')
print("Accomodation:" , f'${user_acc:.1f}')
print("Food:", f'${user_foo:.1f}')
print("---------------------------------------")
print("Ramining Balance:", f'${rem_bal:.1f}')
print("TAXES:", f'${tax:.1f}')
print("Total:", f'${rem_bal:.1f}')


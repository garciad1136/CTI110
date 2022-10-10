# P2LAB1
# 10/02/2022
# CTI-110 P2LAB1 - Driving Cost
# Diosman Garcia

#this function returns the driving cost

#first argument is value of miles
#second argument is value of miles per gallon
#third argument is value of dollers per gallon

# Use the following calculation so it gives the cost in doller
def driving_cost(driven_miles,driven_miles_per_gallon,dollers_per_gallon):
    return (driven_miles/driven_miles_per_gallon)*dollers_per_gallon
    
#Enter the value of miles per gallon
milesPerGallon = float(input())
#Enter the value of dollers per gallon
dollersPerGallon = float(input())
#calculate the driving cost per mile
cost_per_mile = driving_cost(1,milesPerGallon,dollersPerGallon)
#To calculate driving cost of 20 miles multiply the cost of 1 mile with 20
cost_of_20_miles = 20*cost_per_mile
#To calculate driving cost of 75 miles multiply the cost of 1 mile with 75
cost_of_75_miles = 75*cost_per_mile
#To calculate driving cost of 500 miles multiply the cost of 1 mile with 500
cost_of_500_miles = 500*cost_per_mile
#print the output for each with 2 digits after the decimal point 
print(f'{cost_of_20_miles:.2f} {cost_of_75_miles:.2f} {cost_of_500_miles:.2f}')
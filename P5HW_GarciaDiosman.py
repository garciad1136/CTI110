# Math Calculator Quiz
# 11/27/2022
# CTI-110 P5HW2 - Math Quiz
# Diosman Garcia

######PSEUDOCODE-START######
#
# define the addrandom fuction
# ask the user for the input
# initiate the while loop
# define the subrandom fuction
# ask the user for the input
# initiate the while loop
# define the main fuction
# print the main menu and options
# define what option initiate which fuction
# get user option
# print the quiz display message
# 
######PSEUDOCODE-ENDS######

import random
# Defined function for addition
def addrandom():
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("   ",a)
    print(" + ",b)
    # Defined the sum
    sum = a+b
    # Ask users for their answer
    answer = int(input("\nEnter answer: "))
    # Variable to count guesses
    guess = 1
    # Inigiate the loop for getting answer while answer is not correct
    while sum!=answer:
        # If the answer is less than sum print it is too low
        if answer<sum:
            print("Sorry, guess is too low.")
        # If the answer is more than sum print it is too high
        else:
            print("Sorry, guess is too high.")
        # Ask users for their input
        answer = int(input("\ntry again: "))
        # Incress the count of gueses
        guess+=1
    # Print congratulation if answer is correct
    print("Congratulations!!!! your answer is correct....")
    # Print the number of gueses
    print("Number of guesses: ",guess)

# Defined function for subtraction
def subrandom():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    # Defined the difference
    diff = a - b
    # Ask users for their answer
    answer = int(input("\nEnter answer: "))
    # Variable to count guesses
    guess = 1
    # Inigiate the loop for getting answer while answer is not correct
    while diff != answer:
        # If the answer is less than sum print it is too low
        if answer < diff:
            print("Sorry, guess is too low.")
        # If the answer is less than sum print it is too high
        else:
            print("Sorry, guess is too high.")
        # Ask users for their input
        answer = int(input("\ntry again: "))
        # Incress the count of gueses
        guess += 1
    # Print congratulation if answer is correct
    print("Congratulations!!!! your answer is correct....")
    # Print the number of gueses
    print("Number of guesses: ", guess)

# Defined the function for the display menu
def main():
    # displaying menu
    print("\nMain Menu")
    print("----------------------")
    print("1. Addition Random Numbers")
    print("2. Subtraction Random Numbers")
    print("3. Exit\n")
    # Getting the user input
    option = int(input("Please choose one of the option: "))
    # If option equals to 1 initiate the addrandom() function
    if option==1:
        addrandom()
    # If option equals to 2 initiate the subrandom() function
    elif option==2:
        subrandom()
    # If option equals to 3 exit the program
    elif option == 3:
        print("Thank you for playing..")
        print("Bye!!")
        exit()
    # Else print invalid option
    else:
        print("Invalid option. Please choose again")
    # Continue to call the function until user exits the program
    main()


print("Welcome to the Math Quiz\n")
main()

# CTI-110 
# P4HW1 - Score List
# Diosman Garcia
# 11/18/2022

####This program will convert score into grade letter for users####

######PSEUDOCODE-START######
#
# START
# Get the number of scores from the user.
# Declare a list to store to the numbers.
# Get the score from user.
# Check if they lie between 1 to 100
# if yes then add it to the list
# else get score until a correct number is entered
# Print the minimum number in the list.
# Remove the minimum number from the list and print the list.
# Calculate the average of the list and print it.
# Calculate the grade of the list.
# if average is between 91 to 100 then print grade A 
# else if average is between 81 to 90 then print grade B
# else if average is between 71 to 80 then print grade C
# else if average is between 61 to 70 then print grade D
# else if average is between 51 to 60 then print grade E
# else print grade F
# END
#
######PSEUDOCODE-ENDS######

# Prompts user to enter the number of scores.
# Stores the input in variable num_score.
num_score = int(input("How many scores do you want to enter? "))
print()
# Declares an empty list that store all the scores entered.
score_list = []
# Initiat the loop from 0 to num_score-1. 
for i in range(num_score):
    # Prompts the user to enter a score and stores it in a variable score.
    score = int(input("Enter a score #"+str(i+1)+": "))
    # Checks if score lies between 1-100.
    # Initiat loop prints an error message until a correct score is entered.
    while(score<1 or score>100):
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        score = int(input("Enter score #"+str(i+1)+" again: "))
    # Convert score to a float and add it to the list.
    score_list.append(float(score))
print()
    
# Print the results from the list.
print("\n----------------Results----------------")
# Create and store the minimum number in a variable low_score and print it.
low_score = min(score_list)
# Print the Lowest Score.
print("Lowest Score  :",low_score)
# Remove the low_score from the score_list.
score_list.remove(low_score)
# Print the Modified List.
print("Modified List :",score_list)
# Create and store the average score number in a variable avg_score and print it
avg_score = sum(score_list)/len(score_list)
# Add the .2 decimal point to the score and print.
print("Scores Average: %.2f" %avg_score)
# Calculate the grade according to the average and print the grade letter.
if(avg_score>90 and avg_score<=100):
    print("Grade         : A")
elif(avg_score>80 and avg_score<=90):
    print("Grade         : B")
elif(avg_score>70 and avg_score<=80):
    print("Grade         : C")
elif(avg_score>60 and avg_score<=70):
    print("Grade         : D")
elif(avg_score>50 and avg_score<=60):
    print("Grade         : E")
else:
    print("Grade         : F")
print("---------------------------------------")



#Name: PaulGayle
#Date: 04/12/2024
#Assignment Name: P4HW1_GaylePaul
#Description: Assignment tests student's ability to edit and enhance exiting programs.

#Asking the user for the number of scores.
num_of_grades = int(input("How many scores do you want to enter? "))

#Create an empty list to store scores.
module_scores = []
 
#Loop to collect scores.
for num in range(num_of_grades):
    #Keeping track whether the score entered is valid.
    valid_score = False

    #Loop until valid score is entered.
    while not valid_score:
        #Ask the user to enter a number.
        score = input(f"Enter score #{num+1}: ")

        #Check if the input is a number.
        if score.isdigit():
            #Convert score into a float.
            score = float(score)

            #Check if score is within valid range
            if 0 <= score <= 100:
               #If the score is valid, add it to scores list.
               module_scores.append(score)
               valid_score = True
            else:
               #If the score is not valid, notify the user and continue the loop.
               print("Score must be between 0 and 100. Please try again.")
        else:
         #If the input is not a number, notify the user and continue the loop.
            print("Invalid input, please enter a valid score")
           

#Calculating the lowest grade
lowest_grade = min(module_scores)
#Calculating the highest grade
highest_grade = max(module_scores)
#Find the sum of all grades 
sum_of_grades = sum(module_scores)
#Finding the length of all grades
length_of_grades = len(module_scores)
#Calculating the average of all grades
average = sum_of_grades / (num_of_grades)
#Creating input for grade
grade = () 

if average >= 90 and average <= 100:
    grade = ("A")
elif average >= 80 and average < 90:
    grade = ("B")
elif average >=70 and average < 80:
    grade = ("C")
elif average >=60 and average < 70:
    grade = ("D")
else:
    grade = ("F")
          

#Output --------Results-------
print("--------Results-------")
#Output Lowest Grade
print("Lowest Grade:  " +  f'{lowest_grade:.2f}')
#Output Highest Grade
print("Highest Grade: " + f'{highest_grade:.2f}')
#Output Sum      
print("Sum of Grades: " + f'{sum_of_grades:.2f}')
#Output Average
print("Average:       " + f'{average:.2f}')
#Output grade
print("Grade:         " + f'{grade}')
#Output ----------------------
print("----------------------")


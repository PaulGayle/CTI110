#Name: PaulGayle
#Date: 03/06/2024
#Assignment Name: P2HW2_GaylePaul
#Description: Assignment tests the student's understanding of lists.

#module1_grade <--- input("Enter grade for module 1: ")
module1_grade = input("Enter grade for module 1: ")
#module2_grade <--- input("Enter grade for module 2: ")
module2_grade = input("Enter grade for module 2: ")
#module3_grade <--- input("Enter grade for module 3: ")
module3_grade = input("Enter grade for module 3: ")
#module4_grade <--- input("Enter grade for module 4: ")
module4_grade = input("Enter grade for module 4: ")
#module5_grade <--- input("Enter grade for module 5: ")
module5_grade = input("Enter grade for module 5: ")
#module6_grade <--- input("Enter grade for module 6: ")
module6_grade = input("Enter grade for module 6: ")

#module_grade_list <--- [float(module1_grade), float(module2_grade), float(module3_grade), float(module4_grade), float(module5_grade), float(module6_grade)]
module_grade_list = [float(module1_grade), float(module2_grade), float(module3_grade), float(module4_grade), float(module5_grade), float(module6_grade)]
#lowest_grade <--- min(module_grade_list)
lowest_grade = min(module_grade_list)
#highest_grade <--- max(module_grade_list)
highest_grade = max(module_grade_list)
#sum_of_grades <--- sum(module_grade_list)
sum_of_grades = sum(module_grade_list)
#length_of_grades <--- len(module_grade_list)
length_of_grades = len(module_grade_list)
#average <--- sum_of_grades / length_of_grades
average = sum_of_grades / length_of_grades

#Results <--- print("--------Results-------")
print("--------Results-------")
#Lowest Grade <--- print("Lowest Grade:  " +  f'{lowest_grade:.2f}')
print("Lowest Grade:  " +  f'{lowest_grade:.2f}')
#Highest Grade <--- print("Highest Grade: " + f'{highest_grade:.2f}')
print("Highest Grade: " + f'{highest_grade:.2f}')
#Sum <--- print("Sum of Grades: " + f'{sum_of_grades:.2f}')      
print("Sum of Grades: " + f'{sum_of_grades:.2f}')
#Average <--- print("Average:       " + f'{average:.2f}')
print("Average:       " + f'{average:.2f}')
print("----------------------")


#Name: Paul Gayle
#Date: 03/22/2024
#Assignment Name: P3HW2_Salary_GaylePaul
#Assignment Description: Assignment shows students knowlege on creating and displaying using if and else statements.

#employess_name <---- input("Enter employee's name: ")
employees_name = input("Enter employee's name: ")
#hours_worked <--- float(input("Enter number of hours worked: "))
hours_worked = float(input("Enter number of hours worked: "))
#pay_rate <--- float(input("Enter employee's pay rate: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Calculate overtime and gross income using if and else statement
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

#gross_pay variable <--- gross_pay = regular_pay + overtime_pay         
gross_pay = regular_pay + overtime_pay    


print("---------------------------")
#Displaying employee name
print(f'Employee name: {employees_name}')

#Displaying hours worked, pay rate, overtime hours, overtime pay, and gross pay
print(f'Hours worked   Pay Rate   Overtime Hours  RegHour Pay   Overtime Pay   Gross Pay')
print("--------------------------------------------------------------------------------")
print(f'{hours_worked:<15.2f}{pay_rate:<13.2f}{overtime_hours:<13}${regular_pay:<15.2f}${overtime_pay:<12.2f}${gross_pay:.2f}')      

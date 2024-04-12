#Name: Paul Gayle
#Date: 03/11/2024
#Assignment Name: P3LAB
#Description: Assignment shows knowledge on branching and if statements.

is_leap_year = False
   
input_year = int(input("Enter a year."))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False
    



if is_leap_year == True:
    print(f'{input_year} - leap year. ')
else:
    print(f'{input_year} - not a leap year.')

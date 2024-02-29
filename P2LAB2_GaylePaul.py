#Name: Paul Gayle
#Date: 02/29/2024
#Assignment Name: P2LAB2_GaylePaul
#Description: Assignment shows knowledge of how to write code that dis[alys information to users.


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num_list =[num1, num2, num3, num4,]
total_number = num1 + num2 + num3 + num4
average_num = total_number/len(num_list)


product = num1 * num2 * num3 * num4
print(f'{product:.0f}', f'{average_num:.0f}') 
print(f'{product:.3f}', f'{average_num:.3f}')

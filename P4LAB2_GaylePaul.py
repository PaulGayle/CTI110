#Name: Paul Gayle
#Date: 04/03/2024
#Assignment: P4LAB2
#Description: Assignment test students knowledge of if-else statements and while loops




int1 = int(input("Enter first integer. "))
int2 = int(input("Enter second integer. "))

if int2 < int1:
    print("Second integer can't be less than the first")
else:
    print(int1, end=" ")

while int1 + 5 <= int2:
    int1 += 5
    print(int1, end=" ")


#Name: Paul Gayle
#Date: 02/27/2024
#Assignment Name: P2LAB1
#Description: This assignments test the knowlegde of writing code that performs mathmatical calculations and displays to users.





mpg = float(input())
cost_per_gallon = float(input())

distance_20_miles = 20
distance_75_miles = 75
distance_500_miles = 500

gallons_needed_20 = distance_20_miles / mpg
gallons_needed_75 = distance_75_miles / mpg
gallons_needed_500 = distance_500_miles /mpg

total_cost1 = gallons_needed_20 * cost_per_gallon
total_cost2 = gallons_needed_75 * cost_per_gallon
total_cost3 = gallons_needed_500 * cost_per_gallon

print(f"{total_cost1:.2f} {total_cost2:.2f} {total_cost3:.2f}")                          

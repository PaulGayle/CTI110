#Name: PaulGayle
#Date:02/20/2024
#Assignment Name: P1HW2
#Description: This assignment will test the users knowledge of creating programs that do basic math.


print("This program calculates and displays travel expenses")
budget = input("Enter Budget: ")
destination = input("Enter your travel destination: ")
gas = input("How much do you think  you will spend on gas? ")
hotel = input("Approximately, how much you will need for accomadation/hotel? ")
food = input("Last, how much do you need for food? ")
end_budget = int(budget) - int(gas) - int(hotel) - int(food) 

print("----------Travel Expenses---------")
print("Location: " + str(destination))
print("Initial Budget: " + str(budget))

print("Fuel: " + str(gas))
print("Accomadation: " + str(hotel))
print("Food: " + str(food))

print("Remaining Balance: " + str(end_budget))



#Name: Paul Gayle
#Date: 04/26/2024
#Assignment Name: P5HW_GaylePaul
#Description: Assignment shows students knowledge of functions and loops

import random

        
        
def generate_numbers():
    num1 = int(random.randint(1, 500))
    num2 = int(random.randint(1, 500))
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def main_menu():
    print("MAIN MENU")
    print("--------------")
    print("1. Adding Random numbers")
    print("2. Subtracting Random numbers")
    print("3. Exit")



def main():
     while True:
        main_menu()
        choice = input("Please choose one of the options. ")

        if choice == '1':
          num1, num2 = generate_numbers()           
          result = add_numbers(num1, num2)
          num_guesses = 0
          while True:
                print(' ', num1)
                print('+', num2)
                guess = int(input())
                num_guesses += 1
                if guess == result:
                    print(f"Congratulations! You guessed correctly in {num_guesses} guesses.")
                    break
                elif guess < result:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")
        elif choice == '2':
            num1, num2 = generate_numbers()
            result = subtract_numbers(num1, num2)
            num_guesses = 0
            while True:
                print(' ', num1)
                print('-', num2)
                guess = int(input())
                num_guesses += 1
                if guess == result:
                    print(f"Congratulations! You guessed correctly in {num_guesses} guesses.")
                    break
                elif guess < result:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")
        elif choice == '3':
            print("Thank you for playing...")
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()  








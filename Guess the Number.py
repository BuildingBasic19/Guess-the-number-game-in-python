# number selection by the computer
import random # random module is imported to generate random numbers
computer_number = random.randint(1, 100)

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100. Try to guess it!")
print("You have 8 attempts to guess the number.")

def guess_the_number_funk():
    for i in range(1,9):
        guess_the_number = int(input("Enter your guess: "))
        print(8-i,"Chance left")
        if guess_the_number > computer_number:
            print("DOWN")
        elif guess_the_number < computer_number:
            print("UP")
        elif guess_the_number == computer_number:
            print("Your guess was correct")
        else:
            print("invalid input,enter a number between 1 to 100")
    print("the correct answer was",computer_number)

guess_the_number_funk()
    
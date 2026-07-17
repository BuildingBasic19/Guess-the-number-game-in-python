# Guess the Number Game (Python)

A simple command-line game built with Python where the computer randomly selects a number between **1 and 100**, and the player has **8 attempts** to guess it.

After each guess, the game provides a hint:

* **UP** – if the guessed number is lower than the secret number.
* **DOWN** – if the guessed number is higher than the secret number.

This project was created to practice Python fundamentals, user input, loops, functions, conditional statements, and random number generation.

## Features

* Random number generation between **1 and 100**
* Maximum of **8 guessing attempts**
* Hints after every incorrect guess
* Displays remaining chances
* Reveals the correct number after the game ends

## Technologies Used

* Python 3
* `random` module
* Functions
* Loops
* Conditional Statements

## Project Structure

```text
Guess-The-Number/
│── guess_the_number.py
└── README.md
```

## How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/guess-the-number.git
```

2. Open the project directory.

```bash
cd guess-the-number
```

3. Run the program.

```bash
python guess_the_number.py
```

## Sample Output

```text
Welcome to the Guess the Number game!
I have selected a number between 1 and 100. Try to guess it!
You have 8 attempts to guess the number.

Enter your guess: 40
7 Chance left
UP

Enter your guess: 80
6 Chance left
DOWN

Enter your guess: 63
Your guess was correct
```

## What I Learned

While building this project, I practiced:

* Using the `random` module
* Writing and calling functions
* Working with loops
* Using conditional statements
* Taking user input
* Building an interactive command-line game

## Future Improvements

* End the game immediately after the correct guess.
* Validate user input to prevent crashes for non-numeric input.
* Add difficulty levels (Easy, Medium, Hard).
* Allow the player to play multiple rounds.
* Maintain a high-score system based on the fewest attempts.
* Display the total number of attempts used.

## Author

**Anant Tripathi**

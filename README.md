# Guess the Number Game

A simple command-line game developed in Java where the computer randomly selects a number, and the player attempts to guess it. After each guess, the program provides feedback indicating whether the guess is too high or too low until the correct number is found.

This project was built to practice Java programming fundamentals, loops, conditional statements, user input, and random number generation.

## Features

* Randomly generates a secret number
* Accepts user input through the terminal
* Provides hints ("Too High" or "Too Low")
* Counts the number of attempts
* Displays a congratulatory message when the correct number is guessed

## Technologies Used

* Java
* Scanner Class
* Random Class
* Loops
* Conditional Statements
* Methods (if implemented)

## Project Structure

```text
Guess-The-Number/
│── GuessTheNumber.java
└── README.md
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/guess-the-number.git
```

2. Open the project directory.

```bash
cd guess-the-number
```

3. Compile the program.

```bash
javac GuessTheNumber.java
```

4. Run the program.

```bash
java GuessTheNumber
```

## Sample Output

```text
Welcome to Guess the Number!

Guess a number between 1 and 100: 45
Too Low!

Guess a number between 1 and 100: 72
Too High!

Guess a number between 1 and 100: 61
Congratulations! You guessed the correct number in 3 attempts.
```

## Learning Outcomes

This project helped me practice:

* User input using `Scanner`
* Random number generation using `Random`
* Loops (`while` / `do-while`)
* Conditional statements (`if-else`)
* Variables and basic program logic
* Building an interactive command-line application

## Future Improvements

* Add difficulty levels (Easy, Medium, Hard)
* Limit the number of attempts
* High score tracking
* Play Again option
* Graphical User Interface (GUI) using Java Swing or JavaFX

## Author

**Anant Tripathi**

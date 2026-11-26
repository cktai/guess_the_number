# guess_the_number game

our file main.py contains two number-guessing games. They're mirror images of each other: in one you guess, in the other the computer guesses.

Game 1: guess(x), you guess the computer's number
Lines 15–25

The computer secretly picks a random number from 1 to x (line 16).
You type a guess (line 19).
The computer tells you "Too low" or "Too high" (lines 20–23).
This repeats until your guess matches (line 18).
It prints a congratulations message (line 25).

Guess a number between 1 and 10: 5
Sorry, guess again. Too low.
Guess a number between 1 and 10: 8
Sorry, guess again. Too high.
Guess a number between 1 and 10: 7
Yay, congrats. You have guessed the number 7 correctly!!
Game 2: computer_guess(x), the computer guesses your number
Lines 31–47

You think of a number from 1 to x and keep it in your head.
The computer guesses a random number in the range it still thinks is possible (lines 37–40).
You answer H (too high), L (too low), or C (correct) (line 41).
The computer shrinks its range based on your answer (lines 42–45).
This repeats until you type C (line 35).
It prints a success message (line 47).

Is 3 too high (H), too low (L), or correct (C)?? l
Is 9 too high (H), too low (L), or correct (C)?? h
Is 7 too high (H), too low (L), or correct (C)?? c
Yay! The computer guessed your number, 7, correctly!
Side by side
Game 1: guess	Game 2: computer_guess
Who picks the secret number?	Computer	You
Who guesses?	You	Computer
Who says high or low?	Computer	You
Loop stops when...	guess == random_number	feedback == 'c'
Which game runs right now?
Only Game 2, because the last line (main.py:51) is computer_guess(10). Game 1 is defined but never called. To play it, change that line to guess(10), or add guess(10) on its own line to play both.

The comments at the top (lines 3–9) already list the main Python ideas used in the file: functions, while loops, if/elif, input()/print(), random.randint, and f-strings.


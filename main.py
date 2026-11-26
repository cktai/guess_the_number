#The script has two number-guessing games. In the first, you guess the computer's number. In the second, the computer guesses yours.

# Key ideas used:
# Functions (def)	guess and computer_guess
# while loops	Repeating until the right answer
# if / elif	Deciding between too high and too low
# input() / print()	Talking to the player
# random.randint	Picking random numbers
# f-strings	Putting variables into messages



import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

#You think of a secret number, and the computer keeps narrowing down the range where it could be until it lands on it.



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        #If there's more than one number left → pick a random one from the range.Otherwise (only one number left) → guess that number.
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

#computer_guess(10) starts the game where the computer guesses a number you're thinking of, between 1 and 10.

computer_guess(10)

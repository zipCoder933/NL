# NL
A Natural-Language programming language.
Built using Codex.

## How it works

### Writing in NL
* Every command is separated by a line-break
* Make sure to keep the number of stuff per-line to a minimum. Doing so will result in better compilation.
* comments are put in-between parentheses

### Example: Guessing game.
Compiling a guessing game program looks something like this:
First you write the code in NL:

```
(the following is a guessing game)
create a maximum number of 100

Repeat forever...
Store a number between 1 and the maximum number. Call it the answer.
Increase the maximum number by 20
Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
Repeat 14 times...
Ask the user for a guess, and Convert it to a number
if the guess is equal to the answer, congrad the user and end the loop.
otherwise if the guess is higher or lower than the answer, tell the user.
Tell the user how many chances are left.
when the loop has ended, if the user has not guessed the answer, tell the user game over and then exit the game
```

When you compile the code, it gets copied into a directory and gets auto-indented:
```
Create a maximum number of 100

Repeat forever...
    Store a number between 1 and the maximum number. Call it the answer.
    Increase the maximum number by 20.
    Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
    Repeat 14 times...
        Ask the user for a guess, and Convert it to a number
        If the guess is equal to the answer, congradulate the user and end the loop.
        Otherwise if the guess is higher or lower than the answer, tell the user.
        Tell the user how many chances are left.
    When loop has ended, If user has not guessed the answer, tell the user game over and then exit the game.
```

The auto-indented code gets converted to python code and run:

```{:.language-python}
import random

# CMD: Create a maximum number of 100
max = 100
# CMD: Repeat forever...
while True:
    # CMD: Store a number between 1 and the maximum number. Call it the answer.
    answer = random.randint(1,max)
    # CMD: Increase the maximum number by 20.
    max = max + 20
    # CMD: Tell the user that you are thinking of a number between 0 and the maximum number. Tell the user that they only have 14 chances to get it right.
    print("I am thinking of a number between 0 and " + str(max))
    # CMD: Repeat 14 times...
    for i in range(0,14):
        # CMD: Ask the user for a guess, and Convert it to a number
        guess = int(input("Guess a number:"))
        # CMD: If the guess is equal to the answer, congradulate the user and end the loop.
        if guess == answer:
            print("You guessed it!")
            break;
        # CMD: Otherwise if the guess is higher or lower than the answer, tell the user.
        elif guess > answer:
            print("Your guess is too high")
        else: 
            print("Your guess is too low")
        # CMD: Tell the user how many chances are left.
        print("You have " + str(14 - i) + " chances left")
    # CMD: When loop has ended, If user has not guessed the answer, tell the user game over and then exit the game.
    if guess != answer:
        print("Game over")
        exit()
```

## API
List of commands
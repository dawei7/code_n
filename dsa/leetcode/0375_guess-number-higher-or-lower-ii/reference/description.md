## Description

We play a guessing game with these rules:

- One number is chosen from `1` through `n`.
- You repeatedly guess a number.
- A correct guess wins immediately.
- After an incorrect guess, you learn whether the chosen number is higher or lower and continue guessing.
- An incorrect guess `x` costs `x` dollars. Running out of money loses the game.

Given `n`, return the minimum amount of money that guarantees a win regardless of which number was chosen.

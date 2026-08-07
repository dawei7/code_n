### 1. Description

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).

- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).

- `0`: your guess is equal to the number I picked (i.e. $num = pick$).

Return *the number that I picked*.

### 2. Function Contract

**Inputs**

- `n`: The inclusive upper bound of the search range.
- `pick`: Only the app adapter receives the hidden chosen number so it can emulate `guess`; the native LeetCode method receives only `n`.

**Return value**

Return the fixed hidden number identified through the `guess(num)` responses.

### 3. Examples

#### Example 1

- **Input:** $n = 10, pick = 6$
- **Output:** `6`
#### Example 2

- **Input:** $n = 1, pick = 1$
- **Output:** `1`
#### Example 3

- **Input:** $n = 2, pick = 1$
- **Output:** `1`

### 4. Constraints

- $1 \le n \le 2^{31} - 1$

- $1 \le pick \le n$
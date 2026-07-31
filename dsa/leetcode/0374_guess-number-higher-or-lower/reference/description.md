## Description

We play a guessing game in which one fixed number `pick` is chosen from the inclusive range `[1,n]`. Your task is to identify it.

After each incorrect guess, you learn whether `pick` is higher or lower. The predefined API `int guess(int num)` returns:

- `-1` when `num > pick`, meaning the guess is too high.
- `1` when `num < pick`, meaning the guess is too low.
- `0` when `num == pick`.

Return the chosen number.

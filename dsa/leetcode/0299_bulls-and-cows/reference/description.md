## Description

In the Bulls and Cows game, you choose a secret number and a friend attempts to guess it. After a guess, report two kinds of matches:

- A **bull** is a guessed digit that is already in the correct position.
- A **cow** is a non-bull guessed digit that occurs in the secret at a different position. Equivalently, it is one of the remaining digits that could be rearranged to create an additional bull.

Given the strings `secret` and `guess`, return the hint in the form `"xAyB"`, where `x` is the bull count and `y` is the cow count. Both strings may contain repeated digits, and each occurrence can be matched at most once.

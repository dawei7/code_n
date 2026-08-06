## Description

A password is strong only when all of these conditions hold:

- Its length is at least $6$ and at most $20$ characters.
- It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It has no run of three equal consecutive characters. For example, `"Baaabb0"` is weak because of `"aaa"`, while
  `"Baaba0"` satisfies this repetition rule.

Given `password`, return the minimum number of single-character steps needed to make it strong, or `0` when it is
already strong. One step may insert one character, delete one character, or replace one character with another.

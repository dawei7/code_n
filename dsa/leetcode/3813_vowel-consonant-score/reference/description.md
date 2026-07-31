## Description

You are given a string `s` whose characters are lowercase English letters, spaces, or digits.

Let `v` be the number of vowels in the string, and let `c` be its number of consonants.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`. Every other English letter is a consonant. Spaces and digits are therefore counted as neither.

Define the string's **score** by these two cases:

- When `c > 0`, the score is `floor(v / c)`, meaning that the quotient is rounded down to the nearest integer.
- When `c = 0`, the score is `0`.

Return the score as an integer.

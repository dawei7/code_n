## Description

You are given an array `words` containing $n$ strings. Every string has the same length $m$ and uses only lowercase English letters.

Two strings `s` and `t` are **similar** when some number of applications of the following operation, including zero applications, can make them equal:

- Choose either `s` or `t`.
- Advance every letter of the chosen string by one cyclic alphabet step. In particular, the letter after `'z'` is `'a'`.

Count the index pairs `(i, j)` that satisfy both conditions:

- $i < j$.
- `words[i]` and `words[j]` are similar.

Return the number of qualifying pairs.

## Description

You are given a positive integer `n` and an integer `target`.

Construct an integer array of length `n` satisfying both conditions:

- Its elements sum to `target`.
- The absolute values of its elements form a permutation of size `n`; that is, each magnitude from `1` through `n` appears exactly once, with either a positive or negative sign.

Among every array meeting those requirements, return the lexicographically smallest one. If the requested sum cannot be formed, return an empty array.

A permutation of size `n` is any rearrangement of the integers `1,2,...,n`.

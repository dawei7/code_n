## Description

You are given a string `s` of length `n` and an integer array `order`, where `order` is a **<span data-keyword="permutation">permutation</span>** of the numbers in the range `[0, n - 1]`.

Starting from time `t = 0`, replace the character at index `order[t]` in `s` with `'*'` at each time step.

A **<span data-keyword="substring-nonempty">substring</span>** is **valid** if it contains **at least** one `'*'`.

A string is **active** if the total number of **valid** substrings is greater than or equal to `k`.

Return the **minimum** time `t` at which the string `s` becomes **active**. If it is impossible, return -1.

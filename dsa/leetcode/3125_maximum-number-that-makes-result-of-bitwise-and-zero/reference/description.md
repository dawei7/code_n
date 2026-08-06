## Description

Given a positive integer `n`, choose the maximum integer `x` with $x \le n$ such that the bitwise `AND` of every integer in the inclusive range `[x, n]` equals 0.

The range includes both endpoints. Thus a candidate `x` is valid only when applying bitwise `AND` across `x`, `x + 1`, and every subsequent integer through `n` clears every bit position.

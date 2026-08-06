## Description

You are given an inclusive range `[lower, upper]` and a **sorted unique** integer array `nums`, where all elements are within the inclusive range.

A number `x` is considered missing if `x` is in the range `[lower, upper]` and `x` is not in `nums`.

Return *the **shortest succinct** list of ranges that **covers all the missing numbers exactly***. That is, no element of `nums` is included in any of the ranges, and each missing number is covered by one of the ranges.

Each range `[a, b]` in the list should be output as:

- `[a, b]` if $a \neq b$
- `[a, a]` if $a = b$

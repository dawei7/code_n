# Add Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 258 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/add-digits/) |

## Problem Description
### Goal
Given a nonnegative integer `num`, repeatedly replace it with the sum of its decimal digits. Continue applying the same transformation to each multi-digit result until the value lies between `0` and `9`.

Return that final one-digit value, known as the digital root. The input `0` remains `0`, and no intermediate decimal digit may be omitted. Meet the constant-time, loop-free follow-up by using the number's modular pattern rather than constructing every intermediate digit sum, while still handling positive multiples of nine correctly as `9` rather than `0`.

### Function Contract
**Inputs**

- `num`: a nonnegative integer

**Return value**

The final one-digit digital root.

### Examples
**Example 1**

- Input: `num = 38`
- Output: `2`

**Example 2**

- Input: `num = 0`
- Output: `0`

**Example 3**

- Input: `num = 9999`
- Output: `9`

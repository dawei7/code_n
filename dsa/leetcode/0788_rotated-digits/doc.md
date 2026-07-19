# Rotated Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 788 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotated-digits/) |

## Problem Description

### Goal

A positive integer is good when rotating every decimal digit by 180 degrees produces a valid integer different from the original. Digits `0`, `1`, and `8` remain themselves; `2` and `5` exchange; `6` and `9` exchange; and any other digit makes the rotation invalid.

Given `n`, return how many good integers lie in the inclusive range from `1` through `n`. A number containing only unchanged valid digits is not good because its rotation is identical, while one valid changing digit is sufficient when all other digits are rotatable.

### Function Contract

**Inputs**

- `n`: a positive upper bound.

**Return value**

- The number of good rotated integers in the inclusive range `[1, n]`.

### Examples

**Example 1**

- Input: `n = 10`
- Output: `4`
- Explanation: `2`, `5`, `6`, and `9` are valid and change after rotation.

**Example 2**

- Input: `n = 1`
- Output: `0`
- Explanation: Rotating `1` leaves it unchanged.

**Example 3**

- Input: `n = 2`
- Output: `1`
- Explanation: `2` rotates to `5`, so it is good.

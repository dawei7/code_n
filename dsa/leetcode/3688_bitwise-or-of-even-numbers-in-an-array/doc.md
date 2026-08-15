# Bitwise OR of Even Numbers in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3688 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/) |

## Problem Description

### Goal

Inspect every integer in `nums` and retain only the even values. Combine all retained values with the bitwise OR operation and return the resulting integer. A bit is set in the result whenever that bit is set in at least one even array element; odd elements must make no contribution, regardless of their bit patterns.

If the array contains no even number, return 0. This also follows from using 0 as the identity for bitwise OR, because combining 0 with any included even value leaves that value unchanged.

### Function Contract

**Inputs**

- `nums`: A nonempty list of integers, with $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

Return the bitwise OR of exactly the even elements in `nums`, or 0 when none exist.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5, 6]`
- **Output:** `6`

The included values are 2, 4, and 6, whose bitwise OR is 6.

#### Example 2

- **Input:** `nums = [7, 9, 11]`
- **Output:** `0`

No value is even.

#### Example 3

- **Input:** `nums = [1, 8, 16]`
- **Output:** `24`

The included values have distinct high bits, and `8 | 16` equals 24.

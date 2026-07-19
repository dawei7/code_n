# Factorial Trailing Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 172 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/) |

## Problem Description
### Goal
Given a nonnegative integer `n`, consider the factorial $n!$, the product of every positive integer from `1` through `n`. Determine the number of trailing zeroes in its ordinary decimal representation.

Return that trailing-zero count without constructing the potentially enormous factorial. Internal zeroes do not count, and $0!$ as well as $1!$ equals `1`, so both return `0`. Meet the required logarithmic dependence on `n`; the answer may include contributions from factors that supply several powers of ten rather than counting only visibly divisible multiples once.

### Function Contract
**Inputs**

- `n`: nonnegative integer

**Return value**

The count of trailing decimal zeroes in $n!$.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `0`

**Example 2**

- Input: `n = 5`
- Output: `1`

**Example 3**

- Input: `n = 25`
- Output: `6`

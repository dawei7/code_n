# Number of Digit One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 233 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-digit-one/) |

## Problem Description
### Goal
Given a nonnegative integer `n`, write the ordinary decimal representation of every integer in the inclusive interval from `0` through `n`. Count each position containing the digit `1` across all of those representations.

Return the total number of digit-one occurrences, not the number of integers that contain at least one `1`. A value such as `11` contributes twice, while leading zeroes are not written and therefore contribute nothing. The input may be too large to enumerate every number or inspect every produced digit individually, so use the required positional counting complexity.

### Function Contract
**Inputs**

- `n`: a non-negative integer

**Return value**

The total number of digit-one occurrences across all decimal representations in `[0, n]`.

### Examples
**Example 1**

- Input: `n = 13`
- Output: `6`

**Example 2**

- Input: `n = 0`
- Output: `0`

**Example 3**

- Input: `n = 99`
- Output: `20`

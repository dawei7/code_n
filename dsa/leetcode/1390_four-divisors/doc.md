# Four Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1390 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/four-divisors/) |

## Problem Description

### Goal

Given an integer array `nums`, examine the positive divisors of every value independently. A value contributes only when it has exactly four distinct positive divisors; its contribution is the sum of those four divisors.

Values with fewer or more than four divisors contribute zero. Return the sum of all qualifying contributions across the array. Equal values at different positions are separate occurrences and each can contribute.

### Function Contract

**Inputs**

- `nums`: an array of $m$ positive integers, where $1 \le m \le 10^4$ and `nums[i]` is at most $10^5$.

Let $V = \max(\texttt{nums})$.

**Return value**

- The total of the divisor sums for precisely those array entries that have exactly four positive divisors.

### Examples

**Example 1**

- Input: `nums = [21,4,7]`
- Output: `32`
- Explanation: `21` has divisors `1, 3, 7, 21`, while `4` and `7` do not have four divisors.

**Example 2**

- Input: `nums = [21,21]`
- Output: `64`
- Explanation: Each occurrence of `21` contributes `32`.

**Example 3**

- Input: `nums = [8,9,16]`
- Output: `15`
- Explanation: `8` contributes `1 + 2 + 4 + 8`; the square `9` has three divisors, and `16` has five.

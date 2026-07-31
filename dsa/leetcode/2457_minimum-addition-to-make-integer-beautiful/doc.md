# Minimum Addition to Make Integer Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2457 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/) |

## Problem Description

### Goal

You are given positive integers `n` and `target`. Call an integer beautiful when the sum of its decimal digits is at most `target`. For example, the digit sum of `467` is $4+6+7=17$, whereas the digit sum of `500` is $5$.

Find the minimum non-negative integer `x` for which `n + x` is beautiful. Returning `0` is required when `n` already satisfies the digit-sum limit. The inputs guarantee that a suitable addition always exists.

### Function Contract

**Inputs**

- `n`: A positive integer whose digit sum may exceed the limit.
- `target`: A positive upper bound for the resulting digit sum.

The bounds are $1\le n\le 10^{12}$ and $1\le\texttt{target}\le150$.

**Return value**

- The smallest non-negative `x` such that the decimal digit sum of `n + x` is at most `target`.

### Examples

**Example 1**

- Input: `n = 16, target = 6`
- Output: `4`
- Explanation: Adding `4` produces `20`, whose digit sum is $2$. No smaller non-negative addition works.

**Example 2**

- Input: `n = 467, target = 6`
- Output: `33`
- Explanation: Adding `33` produces `500`, whose digit sum is $5$.

**Example 3**

- Input: `n = 1, target = 1`
- Output: `0`
- Explanation: The original number is already beautiful.

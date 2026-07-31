# Count Stepping Numbers in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2801 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-stepping-numbers-in-range/) |

## Problem Description

### Goal

You are given two positive integers, `low` and `high`, as decimal strings. Count the stepping numbers in the inclusive interval from `low` through `high`.

A stepping number has an absolute difference of exactly $1$ between every pair of adjacent digits. A one-digit positive integer therefore qualifies automatically. Leading zeros are not allowed, so they cannot be used to create an alternative representation of a number.

Because the count can be large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `low`: The lower endpoint as a decimal string without leading zeros.
- `high`: The upper endpoint as a decimal string without leading zeros.

Both endpoints contain between $1$ and $100$ digits and satisfy $1 \le \operatorname{int}(\texttt{low}) \le \operatorname{int}(\texttt{high}) < 10^{100}$.

Let $d = \max(\lvert\texttt{low}\rvert, \lvert\texttt{high}\rvert)$.

**Return value**

Return the number of stepping integers in the inclusive interval $[\texttt{low}, \texttt{high}]$, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `low = "1"`, `high = "11"`
- Output: `10`
- Explanation: The qualifying values are the nine one-digit positive integers and `10`.

**Example 2**

- Input: `low = "90"`, `high = "101"`
- Output: `2`
- Explanation: Only `98` and `101` are stepping numbers in this interval.

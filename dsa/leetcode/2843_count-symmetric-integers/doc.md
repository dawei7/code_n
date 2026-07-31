# Count Symmetric Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2843 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-symmetric-integers/) |

## Problem Description

### Goal

You are given two positive integers `low` and `high`. Consider every integer in the inclusive interval from `low` through `high`.

An integer with $2n$ decimal digits is symmetric when the sum of its first $n$ digits equals the sum of its last $n$ digits. An integer with an odd number of digits is never symmetric. Return how many integers in the given interval are symmetric.

### Function Contract

**Inputs**

- `low`: The inclusive lower endpoint of the interval.
- `high`: The inclusive upper endpoint of the interval.

The constraints are $1\le\texttt{low}\le\texttt{high}\le10^4$. Let $R=\texttt{high}-\texttt{low}+1$ denote the number of candidates in the interval.

**Return value**

- The number of symmetric integers in the inclusive interval.

### Examples

**Example 1**

- Input: `low = 1, high = 100`
- Output: `9`
- Explanation: The symmetric values are `11`, `22`, `33`, `44`, `55`, `66`, `77`, `88`, and `99`.

**Example 2**

- Input: `low = 1200, high = 1230`
- Output: `4`
- Explanation: The qualifying values are `1203`, `1212`, `1221`, and `1230`; each has equal digit sums in its two halves.

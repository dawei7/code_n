# Sort Integers by The Power Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1387 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/sort-integers-by-the-power-value/) |

## Problem Description

### Goal

For a positive integer `x`, repeatedly replace it with `x / 2` when it is even and with `3 * x + 1` when it is odd. Its power value is the number of replacements required to reach `1`; the values in the given range are guaranteed to reach `1`.

List every integer from `lo` through `hi`, inclusive, ordered first by increasing power value and then by increasing integer value when powers tie. Return the `k`th integer in this one-indexed order.

### Function Contract

**Inputs**

- `lo`: the inclusive lower bound, with $1 \le \texttt{lo} \le \texttt{hi}$.
- `hi`: the inclusive upper bound, at most $1000$.
- `k`: a one-indexed position within the $R = \texttt{hi} - \texttt{lo} + 1$ integers.
- Let $U$ be the number of distinct Collatz values encountered while evaluating the whole interval.

**Return value**

- The integer occupying position `k` after sorting by `(power value, integer value)`.

### Examples

**Example 1**

- Input: `lo = 12, hi = 15, k = 2`
- Output: `13`

**Example 2**

- Input: `lo = 7, hi = 11, k = 4`
- Output: `7`

**Example 3**

- Input: `lo = 1, hi = 1, k = 1`
- Output: `1`

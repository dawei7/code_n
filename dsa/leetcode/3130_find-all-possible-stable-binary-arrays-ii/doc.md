# Find All Possible Stable Binary Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3130 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/) |

## Problem Description

### Goal

You are given positive integers `zero`, `one`, and `limit`. Construct binary arrays containing exactly `zero` zeroes and exactly `one` ones. Such an array is stable only if every subarray longer than `limit` contains both binary values.

This condition is equivalent to forbidding any consecutive run of zeroes or ones whose length exceeds `limit`; the equal values in a run need not be considered separately as subarrays. Count every stable arrangement of the required multiset and return the result modulo $10^9+7$.

### Function Contract

Let $z=\texttt{zero}$ and $o=\texttt{one}$.

**Inputs**

- `zero`: The exact number $z$ of zeroes in the array, where $1\le z\le1000$.
- `one`: The exact number $o$ of ones in the array, where $1\le o\le1000$.
- `limit`: The greatest permitted length of any equal-value run, where $1\le\texttt{limit}\le1000$.

**Return value**

Return the number of stable binary arrays modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `zero = 1, one = 1, limit = 2`
- **Output:** `2`
- **Explanation:** `[0,1]` and `[1,0]` are the two possible arrangements, and both satisfy the run bound.

#### Example 2

- **Input:** `zero = 1, one = 2, limit = 1`
- **Output:** `1`
- **Explanation:** The limit forces alternating values, leaving `[1,0,1]` as the only valid array.

#### Example 3

- **Input:** `zero = 3, one = 3, limit = 2`
- **Output:** `14`
- **Explanation:** Fourteen arrangements contain three of each value while avoiding three consecutive equal values.

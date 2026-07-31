# Find All Possible Stable Binary Arrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/) |

## Problem Description

### Goal

You are given three positive integers `zero`, `one`, and `limit`. A binary array is stable when it contains exactly `zero` occurrences of `0` and exactly `one` occurrences of `1`.

In addition, every subarray whose length is greater than `limit` must contain at least one `0` and at least one `1`. Equivalently, no consecutive run of equal values may be longer than `limit`. Count all stable binary arrays and return the count modulo $10^9+7$.

### Function Contract

Let $z=\texttt{zero}$ and $o=\texttt{one}$.

**Inputs**

- `zero`: The exact number $z$ of zeroes to place, where $1\le z\le200$.
- `one`: The exact number $o$ of ones to place, where $1\le o\le200$.
- `limit`: The maximum permitted length of a monochromatic run, where $1\le\texttt{limit}\le200$.

**Return value**

Return the number of valid arrays modulo $10^9+7$.

### Examples

**Example 1**

- Input: `zero = 1, one = 1, limit = 2`
- Output: `2`
- Explanation: Both `[0,1]` and `[1,0]` use the required values, and neither contains a run longer than two.

**Example 2**

- Input: `zero = 1, one = 2, limit = 1`
- Output: `1`
- Explanation: Only `[1,0,1]` alternates throughout; the other arrangements contain two adjacent ones.

**Example 3**

- Input: `zero = 3, one = 3, limit = 2`
- Output: `14`
- Explanation: Fourteen arrangements use three of each value without ever placing three equal values consecutively.

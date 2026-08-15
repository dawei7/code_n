# Count Ways To Build Good Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2466 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-ways-to-build-good-strings/) |

## Problem Description

### Goal

Start with an empty string. At each step, choose one of two operations: append `zero` copies of the character `'0'`, or append `one` copies of the character `'1'`. Either operation may be performed any number of times and in any order.

A constructed string is good when its final length is between `low` and `high`, inclusive. Return the number of different good strings that can be produced. Because this count may be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `low`: The minimum permitted good-string length.
- `high`: The maximum permitted good-string length.
- `zero`: The number of zeros appended by a zero operation.
- `one`: The number of ones appended by a one operation.

The constraints are $1\le\texttt{low}\le\texttt{high}\le10^5$ and $1\le\texttt{zero},\texttt{one}\le\texttt{low}$.

**Return value**

- The number of distinct constructible strings with length in the inclusive target range, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `low = 3, high = 3, zero = 1, one = 1`
- **Output:** `8`
- **Explanation:** Every binary string of length three can be built one character at a time.

#### Example 2

- **Input:** `low = 2, high = 3, zero = 1, one = 2`
- **Output:** `5`
- **Explanation:** The good strings are `"00"`, `"11"`, `"000"`, `"011"`, and `"110"`.

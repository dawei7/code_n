# Count the Number of Arrays with K Matching Adjacent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3405 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/) |

## Problem Description

### Goal

You are given integers `n`, `m`, and `k`. Consider arrays `arr` of length $n$ whose elements all lie in the inclusive range $[1,m]$.

An array is good when exactly $k$ indices $i$ with $1\le i<n$ satisfy `arr[i - 1] == arr[i]`. All other adjacent pairs must contain different values. Count how many good arrays exist and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The required array length.
- `m`: The number of permitted values, namely the integers from 1 through $m$.
- `k`: The exact number of matching adjacent pairs.

The constraints are $1\le n,m\le10^5$ and $0\le k\le n-1$.

**Return value**

- The number of good arrays modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 3, m = 2, k = 1`
- **Output:** `4`

The good arrays are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]`, and `[2, 2, 1]`.

#### Example 2

- **Input:** `n = 4, m = 2, k = 2`
- **Output:** `6`

Each valid array has two equal boundaries and one changing boundary. There are three choices for the changing boundary and two choices for the first value.

#### Example 3

- **Input:** `n = 5, m = 2, k = 0`
- **Output:** `2`

Every boundary must change, so the two valid arrays alternate between 1 and 2, starting with either value.

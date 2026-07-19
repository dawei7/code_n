# Find Kth Largest XOR Coordinate Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1738 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) |

## Problem Description

### Goal

The nonnegative integer `matrix` has $m$ rows and $n$ columns. The value of coordinate `(a,b)` is the bitwise XOR of every `matrix[i][j]` in the inclusive rectangle from `(0,0)` to `(a,b)`.

Compute all $mn$ coordinate values conceptually and return their $k$th largest value, where ranks are one-based and repeated values occupy separate ranks. The dimensions are each between $1$ and $1000$, matrix entries are at most $10^6$, and $1 \le k \le mn$.

### Function Contract

**Inputs**

- `matrix`: a nonempty rectangular matrix of nonnegative integers.
- `k`: the one-based descending rank to retrieve.

Let $C=mn$ be the number of matrix cells.

**Return value**

- Return the $k$th largest prefix-rectangle XOR value, counting duplicates separately.

### Examples

**Example 1**

- Input: `matrix = [[5,2],[1,6]], k = 1`
- Output: `7`
- Explanation: The four coordinate values are `5,7,4,0`; the largest is $7$.

**Example 2**

- Input: `matrix = [[5,2],[1,6]], k = 2`
- Output: `5`
- Explanation: Sorting the coordinate values in descending order gives `7,5,4,0`.

**Example 3**

- Input: `matrix = [[5,2],[1,6]], k = 3`
- Output: `4`
- Explanation: The prefix rectangle ending at `(1,0)` has XOR `5 ^ 1 = 4`.

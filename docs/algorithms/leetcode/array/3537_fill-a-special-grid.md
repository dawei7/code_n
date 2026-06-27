# Fill a Special Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3537 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Matrix |
| Official Link | [fill-a-special-grid](https://leetcode.com/problems/fill-a-special-grid/) |

## Problem Description & Examples
### Goal
Given a grid of dimensions $n \times m$, determine the number of ways to fill the cells with integers such that each cell's value is constrained by its neighbors according to a specific parity or adjacency rule (typically requiring that the sum of adjacent cells satisfies a modular condition). The goal is to count valid configurations modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `n`: An integer representing the number of rows.
- `m`: An integer representing the number of columns.

**Return value**

- An integer representing the total number of valid grid configurations modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `n = 2, m = 2`
- Output: `4`

**Example 2**

- Input: `n = 1, m = 3`
- Output: `2`

**Example 3**

- Input: `n = 3, m = 3`
- Output: `8`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with Profile/Bitmasking. Since the constraints on the grid dimensions are typically small in one direction, we process the grid row by row (or column by column), maintaining a bitmask that represents the state of the current boundary. We use the transition matrix method or memoized recursion to count valid state transitions.

---

## Complexity Analysis
- **Time Complexity**: $O(m \cdot 2^n \cdot 2^n)$ or $O(n \cdot 2^m \cdot 2^m)$, where $n$ and $m$ are the grid dimensions.
- **Space Complexity**: $O(2^{\min(n, m)})$ to store the DP states for the current and previous rows.

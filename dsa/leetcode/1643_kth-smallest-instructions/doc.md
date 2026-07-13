# Kth Smallest Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1643 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [kth-smallest-instructions](https://leetcode.com/problems/kth-smallest-instructions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/kth-smallest-instructions/).

### Goal
Find the `k`th lexicographically smallest path instruction string that moves
from `(0, 0)` to the destination using only horizontal `H` and vertical `V`
moves.

### Function Contract
**Inputs**

- `destination`: `[row, column]`.
- `k`: the 1-based lexicographic rank.

**Return value**

The `k`th instruction string.

### Examples
**Example 1**

- Input: `destination = [2, 3], k = 1`
- Output: `"HHHVV"`

**Example 2**

- Input: `destination = [2, 3], k = 2`
- Output: `"HHVHV"`

**Example 3**

- Input: `destination = [2, 3], k = 3`
- Output: `"HHVVH"`

---

## Solution
### Approach
At each position, count how many valid strings would begin with `H` using a
binomial coefficient for the remaining moves. If that count is at least `k`,
append `H`; otherwise append `V` and subtract that count from `k`. Repeat until
all horizontal and vertical moves are placed.

### Complexity Analysis
- **Time Complexity**: `O((row + column)^2)` with precomputed combinations.
- **Space Complexity**: `O((row + column)^2)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

# Construct the Lexicographically Largest Valid Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1718 |
| Difficulty | Medium |
| Topics | Array, Backtracking |
| Official Link | [construct-the-lexicographically-largest-valid-sequence](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/) |

## Problem Description & Examples
### Goal
Construct a sequence of length `2 * n - 1` using one `1` and two copies of every number from `2` to `n`. For every value `x > 1`, the two copies must be exactly `x` positions apart. Return the lexicographically largest valid sequence.

### Function Contract
**Inputs**

- `n`: the largest value to place.

**Return value**

Return one valid lexicographically largest sequence.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `[3,1,2,3,2]`

**Example 2**

- Input: `n = 5`
- Output: `[5,3,1,4,3,5,2,4,2]`

**Example 3**

- Input: `n = 1`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Use backtracking from left to right. At the first empty position, try unused values from `n` down to `1`; for values greater than `1`, place both copies if the paired index is in range and empty. Trying larger values first means the first complete solution is lexicographically largest.

---

## Complexity Analysis
- **Time Complexity**: `O(n!)` worst case search
- **Space Complexity**: `O(n)`

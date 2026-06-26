# Asteroid Collision

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_52` |
| Frontend ID | 735 |
| Difficulty | Medium |
| Topics | Array, Stack, Simulation |
| Official Link | [asteroid-collision](https://leetcode.com/problems/asteroid-collision/) |

## Problem Description & Examples
### Goal
Given an `m x n` matrix where rows are sorted and the first element of each row is greater than the last of the previous row, search for `target`. Return `True` if found.

### Function Contract
**Inputs**

- `matrix`: List[List[int]] (sorted)
- `target`: int

**Return value**

bool - True if target found

### Examples
**Example 1**

- Input: `matrix = [[1, 3, 5, 7], [10, 11, 16, 20]], target = 3`
- Output: `True`

**Example 2**

- Input: `matrix = [[11, 56], [67, 78]], target = 11`
- Output: `True`

**Example 3**

- Input: `matrix = [[17, 25], [31, 35]], target = 35`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.

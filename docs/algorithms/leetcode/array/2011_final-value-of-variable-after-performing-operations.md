# Final Value of Variable After Performing Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2011 |
| Difficulty | Easy |
| Topics | Array, String, Simulation |
| Official Link | [final-value-of-variable-after-performing-operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) |

## Problem Description & Examples
### Goal
Starting from `0`, apply increment and decrement operations represented as strings and report the final value.

### Function Contract
**Inputs**

- `operations`: strings such as `"++X"`, `"X++"`, `"--X"`, and `"X--"`.

**Return value**

Return the final integer value.

### Examples
**Example 1**

- Input: `operations = ["--X","X++","X++"]`
- Output: `1`

**Example 2**

- Input: `operations = ["++X","++X","X++"]`
- Output: `3`

**Example 3**

- Input: `operations = ["X++","++X","--X","X--"]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Each operation containing `'+'` adds one; each operation containing `'-'` subtracts one. Sum those effects.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

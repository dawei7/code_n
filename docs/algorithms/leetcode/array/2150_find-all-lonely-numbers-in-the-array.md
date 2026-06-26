# Find All Lonely Numbers in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2150 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [find-all-lonely-numbers-in-the-array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/) |

## Problem Description & Examples
### Goal
A number is lonely when it appears exactly once and neither adjacent integer, one less or one greater, appears in the array. Return all lonely values in any order.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

A list of all lonely numbers, in any order.

### Examples
**Example 1**

- Input: `nums = [10, 6, 5, 8]`
- Output: `[10, 8]`

**Example 2**

- Input: `nums = [1, 3, 5, 3]`
- Output: `[1, 5]`

**Example 3**

- Input: `nums = [2, 2, 3, 4]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Build a frequency map. A distinct key `x` belongs in the result exactly when its frequency is one and neither `x - 1` nor `x + 1` is a key in the map.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(n)`

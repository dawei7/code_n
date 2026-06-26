# Divide Array Into Equal Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2206 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation, Counting |
| Official Link | [divide-array-into-equal-pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/) |

## Problem Description & Examples
### Goal
Determine whether an even-length array can be partitioned into pairs whose two values are equal.

### Function Contract
**Inputs**

- `nums`: an even-length integer array.

**Return value**

`true` if every element occurrence can belong to an equal-value pair; otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [3, 2, 3, 2, 2, 2]`
- Output: `true`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `false`

**Example 3**

- Input: `nums = [7, 7]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Count occurrences of each value. A complete equal pairing exists exactly when every frequency is even. Equivalently, toggle values in a set and check that the set is empty after the scan.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` expected
- **Space Complexity**: `O(n)`

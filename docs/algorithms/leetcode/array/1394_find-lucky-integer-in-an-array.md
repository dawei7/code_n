# Find Lucky Integer in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1394 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [find-lucky-integer-in-an-array](https://leetcode.com/problems/find-lucky-integer-in-an-array/) |

## Problem Description & Examples
### Goal
A lucky integer is a value whose frequency in the array equals the value itself. Return the largest lucky integer, or `-1` if none exists.

### Function Contract
**Inputs**

- `arr`: a list of integers.

**Return value**

The largest lucky integer in `arr`, or `-1`.

### Examples
**Example 1**

- Input: `arr = [2,2,3,4]`
- Output: `2`

**Example 2**

- Input: `arr = [1,2,2,3,3,3]`
- Output: `3`

**Example 3**

- Input: `arr = [5]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Frequency counting. Count occurrences of each value, then scan the keys for values whose count equals the value and keep the maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(u)` where `u` is the number of distinct values.

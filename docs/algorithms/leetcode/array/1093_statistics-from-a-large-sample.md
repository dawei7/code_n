# Statistics from a Large Sample

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1093 |
| Difficulty | Medium |
| Topics | Array, Math, Probability and Statistics |
| Official Link | [statistics-from-a-large-sample](https://leetcode.com/problems/statistics-from-a-large-sample/) |

## Problem Description & Examples
### Goal
Given a frequency table for values `0` through `255`, compute the minimum, maximum, mean, median, and mode of the represented sample.

### Function Contract
**Inputs**

- `count`: length-256 array where `count[i]` is how many times value `i` appears.

**Return value**

A five-element list `[minimum, maximum, mean, median, mode]` as floating-point values where appropriate.

### Examples
**Example 1**

- Input: `count = [0,1,3,4] + [0]*252`
- Output: `[1,3,2.375,2.5,3]`

**Example 2**

- Input: `count = [2,0,0,1] + [0]*252`
- Output: `[0,3,1.0,0.0,0]`

**Example 3**

- Input: `count = [0,0,5] + [0]*253`
- Output: `[2,2,2.0,2.0,2]`

---

## Underlying Base Algorithm(s)
Frequency-table scanning and order statistics.

---

## Complexity Analysis
- **Time Complexity**: `O(256)`
- **Space Complexity**: `O(1)`

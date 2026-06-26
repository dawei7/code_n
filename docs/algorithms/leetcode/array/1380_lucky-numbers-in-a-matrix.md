# Lucky Numbers in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1380 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [lucky-numbers-in-a-matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) |

## Problem Description & Examples
### Goal
Find every matrix value that is the smallest number in its row and also the largest number in its column.

### Function Contract
**Inputs**

- `matrix`: a rectangular matrix of integers.

**Return value**

A list of all lucky numbers.

### Examples
**Example 1**

- Input: `matrix = [[3,7,8],[9,11,13],[15,16,17]]`
- Output: `[15]`

**Example 2**

- Input: `matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]`
- Output: `[12]`

**Example 3**

- Input: `matrix = [[7,8],[1,2]]`
- Output: `[7]`

---

## Underlying Base Algorithm(s)
Row and column extrema. Compute each row minimum and each column maximum, then select values that belong to both sets.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(m + n)`

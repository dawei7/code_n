# Maximum Side Length of a Square with Sum Less than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1292 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Matrix, Prefix Sum |
| Official Link | [maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) |

## Problem Description & Examples
### Goal
Find the largest side length of a square submatrix whose sum is at most `threshold`.

### Function Contract
**Inputs**

- `mat`: integer matrix.
- `threshold`: maximum allowed square sum.

**Return value**

The maximum valid square side length.

### Examples
**Example 1**

- Input: `mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]`, `threshold = 4`
- Output: `2`

**Example 2**

- Input: `mat = [[2,2],[2,2]]`, `threshold = 1`
- Output: `0`

**Example 3**

- Input: `mat = [[1,0,1],[0,1,0],[1,0,1]]`, `threshold = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
2D prefix sums and incremental side-length testing.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * min(m, n))` in the straightforward scan.
- **Space Complexity**: `O(m * n)`

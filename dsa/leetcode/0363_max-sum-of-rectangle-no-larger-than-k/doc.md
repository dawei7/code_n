# Max Sum of Rectangle No Larger Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 363 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Matrix, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) |

## Problem Description
### Goal
Given a nonempty rectangular integer matrix and an integer limit `k`, choose a nonempty axis-aligned submatrix formed by consecutive rows and consecutive columns. Sum every value inside its rectangular boundaries.

Among rectangles whose sum is at most `k`, return the greatest sum. Sums equal to `k` are allowed and are immediately optimal. Matrix entries may be negative, so enlarging a rectangle does not necessarily increase its sum and the best rectangle need not contain the largest individual values. Return only the optimal sum, not the rectangle coordinates, while meeting the required complexity beyond brute-force enumeration of all cells per rectangle.

### Function Contract
**Inputs**

- `matrix`: a non-empty rectangular matrix of integers
- `k`: the inclusive upper bound for the chosen rectangle's sum

**Return value**

- The greatest rectangular submatrix sum that is at most `k`.

### Examples
**Example 1**

- Input: `matrix = [[1,0,1],[0,-2,3]], k = 2`
- Output: `2`

**Example 2**

- Input: `matrix = [[2,2,-1]], k = 3`
- Output: `3`

**Example 3**

- Input: `matrix = [[-5]], k = -2`
- Output: `-5`

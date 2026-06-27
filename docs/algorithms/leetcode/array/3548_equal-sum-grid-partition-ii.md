# Equal Sum Grid Partition II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3548 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Matrix, Enumeration, Prefix Sum |
| Official Link | [equal-sum-grid-partition-ii](https://leetcode.com/problems/equal-sum-grid-partition-ii/) |

## Problem Description & Examples
### Goal
Determine if a given $m \times n$ grid can be partitioned into four non-overlapping sub-rectangles such that the sum of elements within each sub-rectangle is identical. The partition must be formed by two horizontal cuts and two vertical cuts, effectively dividing the grid into a 3x3 layout where we select four specific regions, or more generally, any configuration of four disjoint rectangles that satisfy the sum equality constraint.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers representing the matrix.

**Return value**

- `bool`: Returns `True` if there exists a partition of the grid into four non-overlapping sub-rectangles with equal sums, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1,2],[3,4],[5,6],[7,8]]`
- Output: `False`

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `True`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem is solved using 2D Prefix Sums to achieve $O(1)$ query time for any sub-rectangle sum. We iterate through all possible valid cut configurations (horizontal and vertical lines). Given the constraints, we optimize by pre-calculating sums and using hash maps or frequency arrays to track reachable sums, effectively reducing the search space from $O(N^4)$ to $O(N^2)$ or $O(N^3)$ depending on the specific partition geometry.

---

## Complexity Analysis
- **Time Complexity**: $O(m^2 \cdot n^2)$, where $m$ is the number of rows and $n$ is the number of columns. This accounts for iterating through all possible cut combinations.
- **Space Complexity**: $O(m \cdot n)$ to store the 2D prefix sum array for efficient range sum queries.

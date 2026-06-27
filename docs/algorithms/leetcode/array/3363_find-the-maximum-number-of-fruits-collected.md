# Find the Maximum Number of Fruits Collected

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3363 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [find-the-maximum-number-of-fruits-collected](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ grid representing a fruit orchard, calculate the maximum number of fruits you can collect by starting at $(0, 0)$ and moving through three specific paths: one moving down-right, one moving down-left, and one moving up-right. Each path must end at the bottom row or the rightmost column, and paths cannot overlap except at the starting point.

### Function Contract
**Inputs**

- `fruits`: A 2D list of integers of size $n \times n$ where `fruits[i][j]` represents the number of fruits at that coordinate.

**Return value**

- An integer representing the maximum total fruits collected across the three defined paths.

### Examples
**Example 1**

- Input: `fruits = [[1,1],[1,1]]`
- Output: `4`

**Example 2**

- Input: `fruits = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `36`

**Example 3**

- Input: `fruits = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]`
- Output: `100`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We decompose the movement into three distinct segments:
1. **Path 1 (Down-Right):** A simple diagonal path from $(0,0)$ to $(n-1, n-1)$.
2. **Path 2 (Down-Left):** A path starting from $(0, n-1)$ moving towards the bottom row.
3. **Path 3 (Up-Right):** A path starting from $(n-1, 0)$ moving towards the right column.
By calculating the maximum fruits for each path independently while respecting the boundary constraints, we aggregate the results.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the grid, as we iterate through the matrix to compute DP states.
- **Space Complexity**: $O(n^2)$ to store the DP table, which can be optimized to $O(n)$ if only the current and previous rows are maintained.

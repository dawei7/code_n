# Largest Local Values in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2373 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [largest-local-values-in-a-matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ integer matrix, generate a new $(n-2) \times (n-2)$ matrix where each element at position $(i, j)$ represents the maximum value found within the $3 \times 3$ subgrid of the original matrix centered at $(i+1, j+1)$.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing an $n \times n$ matrix, where $3 \le n \le 100$.

**Return value**

- A list of lists of integers representing the resulting $(n-2) \times (n-2)$ matrix of local maximums.

### Examples
**Example 1**

- Input: `grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]`
- Output: `[[9,9],[8,6]]`

**Example 2**

- Input: `grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]`
- Output: `[[2,2,2],[2,2,2],[2,2,2]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[9]]`

---

## Underlying Base Algorithm(s)
The problem is solved using a sliding window approach (specifically a 2D convolution-like operation). We iterate through all possible top-left corners of $3 \times 3$ subgrids, calculate the maximum value within each, and store it in the corresponding position of the output matrix.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the input matrix. We visit each of the $(n-2)^2$ subgrids, and for each, we perform a constant number of operations (9 comparisons).
- **Space Complexity**: $O(n^2)$ to store the resulting output matrix.

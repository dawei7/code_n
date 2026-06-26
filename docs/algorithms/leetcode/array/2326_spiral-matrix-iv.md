# Spiral Matrix IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2326 |
| Difficulty | Medium |
| Topics | Array, Linked List, Matrix, Simulation |
| Official Link | [spiral-matrix-iv](https://leetcode.com/problems/spiral-matrix-iv/) |

## Problem Description & Examples
### Goal
The task is to construct an `m x n` matrix by filling its cells in a spiral order using values from a given singly linked list. The matrix should be initialized with a default value of -1. As elements are taken from the linked list, they are placed into the matrix cells following a clockwise spiral path. If the linked list runs out of elements before the entire matrix is filled, the remaining cells should retain their default value of -1.

### Function Contract
**Inputs**

- `m`: An integer representing the number of rows in the matrix.
- `n`: An integer representing the number of columns in the matrix.
- `head`: The head of a singly linked list, which may be `None` if the list is empty. Each node in the list contains an integer value.

**Return value**

- A `List[List[int]]` representing the `m x n` matrix, filled with linked list values in spiral order, or -1 for any unfilled cells.

### Examples
**Example 1**

- Input: `m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]`
- Output: `[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]`

**Example 2**

- Input: `m = 1, n = 4, head = [0,1,2]`
- Output: `[[0,1,2,-1]]`

**Example 3**

- Input: `m = 2, n = 2, head = []`
- Output: `[[-1,-1],[-1,-1]]`

---

## Underlying Base Algorithm(s)
The core algorithm for this problem is **Spiral Traversal** (also known as **Matrix Simulation**). This technique involves using four boundary pointers (top, bottom, left, right) to define the current layer of the matrix being processed. The algorithm iteratively "peels" off layers of the matrix by traversing its perimeter in a clockwise direction:
1.  Traverse from left to right along the `top` row.
2.  Traverse from top to bottom along the `right` column.
3.  Traverse from right to left along the `bottom` row (if `top <= bottom`).
4.  Traverse from bottom to top along the `left` column (if `left <= right`).
After each traversal segment, the corresponding boundary pointer is adjusted inwards. This process continues until the `top` pointer crosses `bottom` or the `left` pointer crosses `right`, or until the linked list is exhausted.

## Complexity Analysis
- **Time Complexity**: `O(m * n)`. We initialize an `m x n` matrix, which takes `O(m * n)` time. Then, we iterate through the matrix cells in a spiral fashion, filling each cell exactly once. In the worst case, we traverse up to `m * n` nodes from the linked list. Therefore, the total time complexity is proportional to the number of cells in the matrix.
- **Space Complexity**: `O(m * n)`. We create an `m x n` matrix to store the result. This is the dominant factor for space complexity. The few boundary pointers and loop variables use `O(1)` additional space.

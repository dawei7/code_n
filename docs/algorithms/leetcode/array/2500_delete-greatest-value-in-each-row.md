# Delete Greatest Value in Each Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2500 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue), Matrix, Simulation |
| Official Link | [delete-greatest-value-in-each-row](https://leetcode.com/problems/delete-greatest-value-in-each-row/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ matrix of integers, perform a series of operations until the matrix is empty. In each operation, remove the largest element from every row. From the set of elements removed in a single operation, identify the maximum value and add it to a running total. Return the final accumulated sum.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the $m \times n$ matrix.

**Return value**

- An integer representing the sum of the maximums of the removed elements across all operations.

### Examples
**Example 1**

- Input: `grid = [[1,2,4],[3,3,1]]`
- Output: `8`
- Explanation: Operation 1: remove 4 and 3 (max is 4). Operation 2: remove 2 and 3 (max is 3). Operation 3: remove 1 and 1 (max is 1). Sum: 4 + 3 + 1 = 8.

**Example 2**

- Input: `grid = [[10]]`
- Output: `10`

**Example 3**

- Input: `grid = [[9,8],[1,6]]`
- Output: `15`

---

## Underlying Base Algorithm(s)
The problem is solved using a greedy simulation approach. By sorting each row in non-decreasing order, we can efficiently access the largest elements in each row sequentially. Since we must remove the largest element from every row simultaneously, sorting allows us to treat the columns of the sorted matrix as the sets of elements removed in each step.

---

## Complexity Analysis
- **Time Complexity**: $O(m \cdot n \log n)$, where $m$ is the number of rows and $n$ is the number of columns. This is dominated by the sorting of each of the $m$ rows.
- **Space Complexity**: $O(1)$ if sorting in-place, or $O(m \cdot n)$ if the input grid is immutable and requires a copy.

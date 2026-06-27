# Minimum Operations to Write the Letter Y on a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3071 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix, Counting |
| Official Link | [minimum-operations-to-write-the-letter-y-on-a-grid](https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ grid of integers (where $n$ is odd), determine the minimum number of cell modifications required to transform the grid such that all cells forming the shape of the letter 'Y' contain the same value $v_1$, and all other cells contain a different value $v_2$ (where $v_1 \neq v_2$). The 'Y' shape is defined as the union of the two diagonals from the top corners meeting at the center, and the vertical line extending from the center to the bottom middle of the grid.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size $n \times n$, where $n$ is odd.

**Return value**

- An integer representing the minimum number of operations (cell value changes) needed to satisfy the 'Y' pattern condition.

### Examples
**Example 1**

- Input: `grid = [[1,2,2],[1,1,0],[0,1,0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]`
- Output: `12`

**Example 3**

- Input: `grid = [[1,2,2,1,2],[2,0,1,1,0],[2,1,2,1,2],[0,2,0,0,2],[1,0,2,2,1]]`
- Output: `14`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Counting/Frequency Analysis** approach. We partition the grid into two sets of cells: those belonging to the 'Y' shape and those that do not. We count the frequency of each digit (0-2) in both sets. Since we must choose two distinct values $v_1$ and $v_2$, we iterate through all possible pairs $(v_1, v_2)$ where $v_1 \neq v_2$, calculate the cost to transform the grid for that pair, and track the minimum cost.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the grid. We traverse the grid once to count frequencies, and the number of possible value pairs is constant (3 values, $3 \times 2 = 6$ pairs).
- **Space Complexity**: $O(1)$, as we only store frequency counts for three possible values (0, 1, 2) in two sets, which is a constant amount of extra space.

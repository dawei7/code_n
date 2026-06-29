# Path With Minimum Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMINPATH |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMINPATH](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMINPATH) |

---

## Problem Statement

Given a `N x M` matrix with non-negative integers, find the minimum sum of path cells from top left cell to bottom right cell. You can only move right or downward from any cell without exiting the matrix boundary.

For eg., in the following matrix :

![matminpath](https://i.ibb.co/4fN9WkZ/Screenshot-2024-03-14-at-3-01-58-PM.png)

Minimum path sum = **13** (highlighted cells are minimum path cells).

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, the minimum sum of path cells from top left cell to bottom right cell

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are non-negative and won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
3 3
4 3 0
8 2 1
3 1 5
```

**Output**

```text
13
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Basic DP.

**Problem:**

Given an N x M matrix with non-negative integers, the task is to find the minimum sum of path cells from the top-left cell to the bottom-right cell. You can only move right or downward from any cell without exiting the matrix boundary.

**Solution Approach:**

The main idea is to use dynamic programming( *why?*, because this problem has both optimal substructure and overlapping subproblems) to efficiently find the minimum sum of path cells from the top-left cell to the bottom-right cell in the given matrix. We initialize a dynamic programming (DP) matrix of the same size as the input matrix and populate it iteratively. By traversing through the DP matrix, we compute the minimum sum for each cell by considering the minimum sum from the cell above and the cell to the left, and adding the value of the current cell from the input matrix. This approach effectively builds the solution bottom-up, ensuring that each cell contains the minimum sum of the path from the top-left cell to that cell. Finally, the value stored in the bottom-right cell of the DP matrix represents the minimum sum of path cells.

**Time Complexity:** O(N * M), as we iterate through all cells of the matrix once to compute the minimum sum.

**Space Complexity:** O(N * M) for the DP matrix, as it stores state information about each cell.

</details>

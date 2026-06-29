# Maximal square of all ones

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMAXSQ |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMAXSQ](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMAXSQ) |

---

## Problem Statement

Given a `N x N` binary matrix, find the area of maximal square submatrix in it which has all 1s.

For eg. in the following matrix, the area of maximal submatrix with all 1's is: **4** (2x2 submatrix)

![matmaxsq](https://i.ibb.co/vXxSJyq/Screenshot-2024-03-14-at-2-33-11-PM.png)

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the no. of rows and columns in the binary matrix.
- Next $N$ lines contains $N$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line the area of maximal square submatrix having all 1's

---

## Constraints

- $1 \leq N \leq 100$
- The elements of the matrix are either `0` or `1`.

---

## Examples

**Example 1**

**Input**

```text
3
0 1 0
0 1 1
0 1 1
```

**Output**

```text
4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops, Basic Dynamic Programming.

**Problem:**

Given an N x N binary matrix, find the area of the maximal square submatrix in it, which consists entirely of 1s.

**Solution Approach:**

Let’s repharse the problem a little bit: *Find the maximal square of all 1s having its bottom-right corner at cell (i, j).*

In order to find the maximal square submatrix ending at cell (i, j), we need to consider the sizes of the square submatrices ending at the three adjacent cells: the cell above (i-1, j), the cell to the left (i, j-1), and the cell diagonally above-left (i-1, j-1). These adjacent submatrices represent the largest square submatrices that can be extended to include the current cell (i, j) while maintaining the condition that all elements within the submatrix are 1s.

By considering these adjacent submatrices, we can determine the size of the maximal square submatrix ending at cell (i, j) as follows:

- If the current cell (i, j) contains a 1, we can extend the square submatrix ending at the cell diagonally above-left (i-1, j-1) by one unit, as long as the cells to its left (i, j-1), above (i-1, j), and diagonally above-left (i-1, j-1) also form a square submatrix of the same size.

- If any of these adjacent cells contain a 0, it indicates that the square submatrix cannot be extended further to include the current cell (i, j). Thus, the size of the square submatrix ending at cell (i, j) will be limited by the minimum of the sizes of the adjacent submatrices plus one.

By updating the dynamic programming matrix (dp) with these considerations, we ensure that each cell (i, j) stores the size of the largest square submatrix ending at that cell. This approach allows us to efficiently compute the maximal square submatrix for each cell in the matrix and determine the overall maximum size of the square submatrix within the entire matrix.

**Time Complexity:**  O(n^{\text{2}}), as we iterate through all cells of the matrix once.

**Space Complexity:** The space complexity is O(n^{\text{2}}) for the DP matrix, as it stores information about each cell of the input matrix.

</details>

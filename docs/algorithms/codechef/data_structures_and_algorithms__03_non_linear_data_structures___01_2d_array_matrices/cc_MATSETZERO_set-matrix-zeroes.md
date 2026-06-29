# Set Matrix Zeroes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATSETZERO |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MATSETZERO](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MATSETZERO) |

---

## Problem Statement

Given an `N x M` integer matrix, if an element is `0`, set its entire row and column to `0`s.

**Note:** You **don’t need to repeat the process for new 0s that are formed** during the operation.

See the following example:

![matsetzero](https://i.ibb.co/RST9jxR/Screenshot-2024-03-14-at-1-40-20-PM.png)

## Function Declaration

### Function Name
$setZeroes$ – This function modifies the given matrix such that if any cell contains `0`, its entire row and column are set to `0`.

### Parameters

* $mat$ : A reference to a 2D integer matrix of size $N \times M$.

### Return Value

* This function does **not** return anything.
* The matrix $mat$ is modified **in-place** according to the rules.

## Constraints

- $1 \leq N, M \leq 1000$
- $0 \leq mat[i][j] \leq 1000$

---

## Input Format

* The first line contains two integers $N$ and $M$ — the number of rows and columns in the matrix.
* The next $N$ lines each contain $M$ space-separated integers representing the matrix elements.

---

## Output Format

* Output the modified matrix of size $N \times M$.
* Each row should be printed on a new line with space-separated integers.

---

## Constraints

- $1 \leq N, M \leq 1000$
- The elements of the matrix are non-negative and won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
3 3
4 6 0
8 2 1
3 1 5
```

**Output**

```text
0 0 0
8 2 0
3 1 0
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops.

**Problem:**

Given an N x M integer matrix, if an element is 0, set its entire row and column to 0’s.

**Solution Approach:**

My idea is simple: store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row 0 and the state of column 0 would occupy the same cell, I let it be the state of row 0, and use another variable  `first_col_zero`  for column 0. In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way.

*Steps* *in* *detail:*

- **Initialization**: Initialize a variable `first_col_zero` to track if the first column contains any zeros.

- **Detection of Zeros**: Traverse through the matrix to detect zeros. If a zero is found at position (i, j), set the corresponding elements in the first row (`mat[0][j]`) and the first column (`mat[i][0]`) to zero.

- **Setting Rows and Columns to Zero**: Traverse through the matrix again, starting from the bottom-right corner. If the first row or column contains a zero (`mat[i][0] == 0` or `mat[0][j] == 0`), set the current element to zero.

- **Handling the First Column**: After processing other columns, if `first_col_zero` is 0, set all elements in the first column to zero.

- **Output**: The matrix is updated with zeros according to the specified conditions.

**Time Complexity:**

- Let N be the number of rows and M be the number of columns in the matrix.

- The time complexity of the solution is O(N * M), as we traverse the entire matrix twice.

**Space Complexity:**

- The space complexity is O(1), as only a few variables are used.

</details>

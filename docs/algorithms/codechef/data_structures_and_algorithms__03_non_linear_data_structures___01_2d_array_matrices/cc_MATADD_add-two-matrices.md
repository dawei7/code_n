# Add Two Matrices

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATADD |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATADD](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATADD) |

---

## Problem Statement

Given two matrices of same size **M x N**, add them and print the resultant matrix.

![matsum](https://i.ibb.co/ykT963y/Screenshot-2024-03-16-at-8-34-23-PM.png)

For eg., here we can see, the sum of matrices `A` and `B` is the matrix `A+B` at the rightmost side.

Let's say we have two matrices A and B of the same dimensions (**M x N**).
The sum of these two matrices, denoted as C = A + B,
is another matrix of
the same dimensions where each element C[i][j] is the sum of the corresponding
elements A[i][j] and B[i][j].

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the number of rows and columns of the two input matrices.
- Next $N$ lines contains $M$ space separated integers, the elements of first matrix.
- Similarly, next $N$ lines contains $M$ space separated integers, the elements of second matrix.

---

## Output Format

Output $N$ lines contains $M$ space separated integers, the elements of resultant matrix.

---

## Constraints

- $1 \leq N, M \leq 1000$
- The elements of both the matrices are non-negative and won't exceed $100000$.

---

## Examples

**Example 1**

**Input**

```text
2 3
2 3 4
4 5 6
1 7 4 
6 4 9
```

**Output**

```text
3 10 8
10 9 15
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Basic Math, Loop

**Problem:** This problem requires adding two matrices of the same size and printing the resultant matrix.

**Solution Approach:**

-

*Addition*: After inputting both matrices, element-wise addition is performed. For each corresponding element in matrices A and B, their sum is calculated and stored in a resultant matrix.

-

*Output*: The resultant matrix, obtained by adding the corresponding elements of matrices A and B, is printed. The elements are printed row by row, separated by space, and each row is printed on a new line.

**Time Complexity**: The time complexity of this solution is O(M * N) since it iterates through all elements of the matrices.

**Space Complexity**: The space complexity is O(M * N) to store the input matrices and the resultant matrix.

</details>

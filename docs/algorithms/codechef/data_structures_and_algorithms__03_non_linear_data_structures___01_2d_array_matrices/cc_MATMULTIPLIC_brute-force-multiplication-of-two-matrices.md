# Brute Force- Multiplication of Two Matrices

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMULTIPLIC |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMULTIPLIC](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMULTIPLIC) |

---

## Problem Statement

Matrix multiplication involves combining the rows of the first matrix with the columns of the second matrix to produce a new matrix. Specifically, let's say we have two matrices A and B, where A has dimensions **M x N** (M rows, N columns), and B has dimensions **N x P** (N rows, P columns). The resulting matrix C from the multiplication, denoted as C = A * B, will have dimensions **M x P**.

To compute the element at position C[i][j] in the resulting matrix C, we take the dot product of the $i^{\text{th}}$ row of matrix A and the $j^{\text{th}}$ column of matrix B.

Mathematically, if A is represented as:

A = [[a11, a12, ..., a1n],
     [a21, a22, ..., a2n],
     ...,
     [am1, am2, ..., amn]]

and B is represented as:

B = [[b11, b12, ..., b1p],
     [b21, b22, ..., b2p],
     ...,
     [bn1, bn2, ..., bnp]]

then the resulting matrix C is calculated as:

C = [[c11, c12, ..., c1p],
     [c21, c22, ..., c2p],
     ...,
     [cm1, cm2, ..., cmp]]

where each element cij in matrix C is computed as:

cij = a[i][1]*b[1][j] + a[i][2]*b[2][j] + ... + a[i][n]*b[n][j]

In other words, each element cij in the resulting matrix C is obtained by multiplying the corresponding elements of the ith row of matrix A with the corresponding elements of the jth column of matrix B and summing up the products.

For eg, see the multiplication of following two matrices:
![matmul](https://i.ibb.co/kHX3qFR/mat-mul.png)

---

## Input Format

- The first line of input will contain two space separated integers $M$ and $N$, denoting the number of rows and columns of the first matrix.
- Next $M$ lines contains $N$ space separated integers, the elements of first matrix.
- Next line contain two space separated integers $N$ and $P$, denoting the number of rows and columns of the second matrix.
- Next $N$ lines contains $P$ space separated integers, the elements of second matrix.

---

## Output Format

Output $M$ lines, each containing $P$ space separated integers, the elements of multiplication matrix of first and second input matrices.

---

## Constraints

- $1 \leq N, M, P \leq 100$
- The elements of both the matrices are non-negative and won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
2 3
2 3 4
4 5 6
3 2
1 2
3 4
2 2
```

**Output**

```text
19 24 
31 40
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Basic Math, Loops

**Problem:** Given two matrix of sizes `n x m` and `m x p` respectively, multiply them.

**Solution Approach:** Lets reiterate the approach mentioned on problem page.

Matrix multiplication is a fundamental operation in linear algebra, where two matrices are multiplied to produce a new matrix. The number of columns in the first matrix must be equal to the number of rows in the second matrix for the multiplication to be defined. Let’s delve into the explanation:

**Reason for Dimension Constraint:**

The reason why the number of columns in the first matrix (m) must be equal to the number of rows in the second matrix (m) is fundamental to the definition of matrix multiplication.

Consider the multiplication of a matrix A (n x m) and a matrix B (m x p). To compute each element c_{ij} of the resulting matrix, we take the dot product of the i-th row of matrix A and the j-th column of matrix B. For this dot product to be defined, the vectors being multiplied must have the same length, which means the number of elements in the row vector of A must be equal to the number of elements in the column vector of B.

If the number of columns in A is not equal to the number of rows in B, the dot product operation is undefined, and therefore, matrix multiplication cannot be performed.

In conclusion, the constraint that the number of columns in the first matrix must be equal to the number of rows in the second matrix ensures that the dot product operation is well-defined for each element of the resulting matrix, enabling matrix multiplication to be performed.

**Time Complexity**:  The time complexity of matrix multiplication using the standard algorithm is O(n * m * p). This arises from the fact that each element of the resulting matrix C (n x p) requires a dot product computation involving m multiplications and additions.

**Space Complexity**:  When performing matrix multiplication out-of-place, the space complexity is O(n * p) for the resulting matrix C, as a new matrix of this size needs to be allocated.

</details>

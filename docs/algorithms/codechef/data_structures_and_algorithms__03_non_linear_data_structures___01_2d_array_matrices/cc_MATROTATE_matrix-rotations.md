# Matrix Rotations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATROTATE |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATROTATE](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATROTATE) |

---

## Problem Statement

Given a `N x N` square matrix, rotate 90° **clockwise**.

For eg. see the following rotation:

![matrotate](https://i.ibb.co/QJ92M0k/Screenshot-2024-03-14-at-11-27-56-AM.png)

## Function Declaration

### Function Name

$rotateClockwise$

### Description

$rotateClockwise$ : rotates a given **N × N square matrix** by **90 degrees clockwise**.
The rotation should be performed **in-place**, meaning the input matrix itself is modified without using any extra matrix.

### Parameters

* $matrix$ : A 2D array of integers of size $N \times N$
  Represents the square matrix to be rotated.

### Return Value

* The function **does not return anything**.
* The input matrix is modified directly to reflect the rotated matrix.

## Constraints

- $1 \leq N \leq 100$
- The elements of the matrix are non-negative and won't exceed $1000$.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the no. of rows and columns in input matrix
- Next $N$ lines contains $N$ space separated integers, the elements of the matrix.

---

## Output Format

- Output $N$ lines, each containing $N$ space separated integers, the elements of rotated matrix.
- **Follow up:** Can you do it in-place by modifying the input matrix, without allocating extra space for another matrix ?

---

## Examples

**Example 1**

**Input**

```text
3
3 1 5
8 2 1
4 6 0
```

**Output**

```text
4 8 3
6 2 1
0 1 5
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1 5
```

**Output for this case**

```text
4 8 3
```



#### Test case 2

**Input for this case**

```text
8 2 1
```

**Output for this case**

```text
6 2 1
```



#### Test case 3

**Input for this case**

```text
4 6 0
```

**Output for this case**

```text
0 1 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Array/Vector, Sorting etc.

**Problem:** Given an N x N square matrix, rotate it 90 degrees clockwise .

**Solution Approach:**

The solution uses two step manipulation on given input matrix.

**Step 1: Reverse Rows (Vertical Flip)**

Reversing the rows of a matrix effectively flips the matrix vertically. Let’s denote the original matrix as A and the matrix after reversing the rows as A’. Consider an example with a 3x3 matrix:

Original Matrix (A):

``1 2 3
4 5 6
7 8 9
``

After reversing rows:

``7 8 9
4 5 6
1 2 3
``

As observed, the rows have been reversed, resulting in a vertical flip of the matrix.

**Step 2: Transpose**

Transposing a matrix involves swapping elements across the diagonal (row-column index exchange). Let’s denote the transposed matrix of A’ as A’'.

Original Matrix (A’):

``7 8 9
4 5 6
1 2 3
``

After transposing:

``7 4 1
8 5 2
9 6 3
``

The rows have become columns and vice versa. This operation effectively rotates the matrix 90 degrees counterclockwise.

**Combining Step 1 and Step 2:**

When we combine reversing the rows and transposing the matrix, we first achieve a vertical flip (Step 1) and then rotate the matrix 90 degrees counterclockwise (Step 2).

Original Matrix (A):

``1 2 3
4 5 6
7 8 9
``

After Step 1 (Reversing Rows):

``7 8 9
4 5 6
1 2 3
``

After Step 2 (Transposing):

``7 4 1
8 5 2
9 6 3
``

The resulting matrix is the original matrix rotated 90 degrees clockwise.

Therefore, combining Step 1 and Step 2 in the provided algorithm rotates the matrix 90 degrees clockwise.

**Time Complexity:**

- Let N be the number of rows (or columns) in the square matrix.

- Reversing Rows: O(N) to reverse N rows.

- Transpose: O(N^2) to traverse and swap elements in the upper triangular part of the matrix.

- Overall time complexity: O(N^2)

**Space Complexity:**

- Since the rotation is performed in-place, the space complexity is O(1), as no additional space is used apart from some constant space for variables used in the algorithm.

</details>

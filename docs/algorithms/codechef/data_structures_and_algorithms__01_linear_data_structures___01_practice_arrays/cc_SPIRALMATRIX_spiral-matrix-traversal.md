# Spiral Matrix Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPIRALMATRIX |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SPIRALMATRIX](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/SPIRALMATRIX) |

---

## Problem Statement

Given an 2D matrix $m \times n$  , return all its elements in **spiral order**.

## Function Declaration

### Function Name

$spiralOrder$ – This function returns the elements of a matrix in spiral order.

### Parameters

* $matrix$ : A 2D array of integers with $m$ rows and $n$ columns.

### Return Value

* Returns an array containing all matrix elements in **spiral order**.

## Constraints

* $1 \leq m, n \leq 10$
* $−100 \leq matrix[i][j] \leq 100$
* The matrix is non-empty

---

## Input Format

* The first line of each test case contains two space-separated integers $m$ and $n$ — the number of rows and columns of the matrix.
* The next $m$ lines each contain $n$ space-separated integers, representing the rows of the matrix.

---

## Output Format

For each test case, output on a new line all elements of the matrix in **spiral order**, separated by spaces.

---

## Constraints

- $m = \text{matrix.length} $
- $n = \text{matrix[i].length} $
- $1 \le m, n \le 10 $
- $-100 \le \text{matrix[i][j]} \le 100$

---

## Examples

**Example 1**

**Input**

```text
3 3
1 2 3
4 5 6
7 8 9
```

**Output**

```text
1 2 3 6 9 8 7 4 5
```

**Example 2**

**Input**

```text
3 4
2 4 6 8
10 12 14 16
18 20 22 24
```

**Output**

```text
2 4 6 8 16 24 22 20 18 10 12 14
```

**Example 3**

**Input**

```text
3 2
5 1
9 2
8 3
```

**Output**

```text
5 1 2 3 8 9
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Restatement

We are given an `m x n` matrix. The task is to print all elements in **spiral order**, starting from the top-left corner and moving clockwise.

---

### Intuition

The spiral pattern can be visualized as peeling the matrix layer by layer:

1. Start from the **top row** (left to right).
2. Then go down the **right column** (top to bottom).
3. Next, traverse the **bottom row** (right to left).
4. Finally, go up the **left column** (bottom to top).
5. After completing one boundary, shrink the limits inward and repeat until all elements are visited.

This continues until either:

* All rows are traversed, or
* All columns are traversed.

---

### Approach

We maintain **four boundaries**:

* `top` → starting row index
* `bottom` → ending row index
* `left` → starting column index
* `right` → ending column index

At each step:

1. Traverse from **left to right** along `top`. Then increment `top`.
2. Traverse from **top to bottom** along `right`. Then decrement `right`.
3. If there are rows remaining, traverse from **right to left** along `bottom`. Then decrement `bottom`.
4. If there are columns remaining, traverse from **bottom to top** along `left`. Then increment `left`.

Repeat this process until `top > bottom` or `left > right`.

---

### Complexity Analysis

* Each element is visited exactly **once**.
* Time Complexity: **O(m × n)**
* Space Complexity: **O(1)** (excluding the output list).

---

### Dry Run Example

For:

```
m = 3, n = 3
1  2  3
4  5  6
7  8  9
```

**Steps:**

* Top row → `1 2 3`
* Right column → `6 9`
* Bottom row → `8 7`
* Left column → `4`
* Remaining center → `5`

**Output:**

```
1 2 3 6 9 8 7 4 5
```

---

### Edge Cases to Consider

1. Single element (`1x1`).
2. Single row (`1 x n`).
3. Single column (`m x 1`).
4. Rectangular matrices (`m != n`).
5. Negative or zero values.

</details>

# Equal Rows and Columns

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATEQRC |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATEQRC](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATEQRC) |

---

## Problem Statement

Given a `N x N` integer matrix, find the no. of pairs of row and column which are equal.

For eg. in the following matrix:

![matmaxsq](https://i.ibb.co/ssQrW5Q/Screenshot-2024-03-16-at-5-41-04-PM.png)

Number of equal pairs of row and columns is: **2** (Row 2 and column 2 are equal. Similarly, row 3 and column 3 are also equal)

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the no. of rows and columns in the matrix.
- Next $N$ lines contains $N$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line the no. of pairs of row and columns which are equal.

---

## Constraints

- $1 \leq N \leq 100$
- The elements of the matrix are non-negative and won't exceed `1000`.

---

## Examples

**Example 1**

**Input**

```text
4
9 0 0 3
0 1 1 5
0 1 1 5
8 5 5 1
```

**Output**

```text
4
```

**Explanation**

Row 2 and column 2 are equal.

Row 2 and column 3 are equal.

Row 3 and column 2 are equal.

Row 3 and column 3 are equal.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Map/HashMap.

**Problem:** Given a `N x N` integer matrix, find the no. of pairs of row and column which are equal.

**Solution Approach:** The main idea of the solution is to count the number of pairs of rows and columns in a given integer matrix that are equal. This is achieved by constructing a map where each key-value pair represents a unique row vector and its frequency in the matrix. Initially, the map is empty. We then iterate through each row of the matrix and insert its vector representation into the map, incrementing the frequency count if the row vector already exists in the map. After constructing the map, we iterate through each column of the matrix. For each column, we construct a vector containing its elements and check the map to find the frequency of this column vector. The frequency represents the number of rows in the matrix that have the same elements in the corresponding column. By summing up these frequencies for each column, we obtain the total count of pairs of equal rows and columns. This approach efficiently handles the problem by leveraging the map data structure to store and manipulate row vectors, resulting in a time complexity of O(N * log N), where N is the size of the matrix.

**Time Complexity**:  O(N*logN + N * M) = O(N * M)

**Space Complexity**:  (N * M), because we’re storing almost entire matrix in map in worst case.

</details>

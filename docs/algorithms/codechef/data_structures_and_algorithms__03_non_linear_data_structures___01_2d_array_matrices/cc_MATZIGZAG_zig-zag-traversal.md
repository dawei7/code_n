# Zig-zag traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATZIGZAG |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATZIGZAG](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATZIGZAG) |

---

## Problem Statement

Given a `N x M` matrix, print its element in zig-zag fashion, i.e., print first row from left to right, second row from right to left, third row again from left to right and so on.

For eg., for the following matrix :

![matzigzag](https://i.ibb.co/Vw5Y8dT/Screenshot-2024-03-14-at-1-07-44-PM.png)

Output should be: 4 6 0 1 2 8 3 1 5

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, $N*M$ elements of the given matrix in zig-zag fashion.

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
4 6 0
8 2 1
3 1 5
```

**Output**

```text
4 6 0 1 2 8 3 1 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops.

**Problem:**

Given an N x M matrix, print its elements in zig-zag fashion, alternating between left-to-right and right-to-left traversal for each row.

**Solution Approach:**

Traverse each row of the matrix. For even-indexed rows (starting from 0), print the elements left-to-right. For odd-indexed rows, print the elements right-to-left.

**Time Complexity:** O(N * M)

**Space Complexity:** O(1) as no additional space was allocated.

</details>

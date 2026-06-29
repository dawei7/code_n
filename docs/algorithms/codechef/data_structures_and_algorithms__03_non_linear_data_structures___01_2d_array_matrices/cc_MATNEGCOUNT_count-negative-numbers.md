# Count Negative Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATNEGCOUNT |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATNEGCOUNT](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATNEGCOUNT) |

---

## Problem Statement

Given a `N x M` matrix which is sorted in non-increasing order both row-wise and column-wise, count the number of negative numbers in matrix.

For eg, in the following matrix:

![matnegcount](https://i.ibb.co/BcZGhR2/Screenshot-2024-03-14-at-11-11-19-PM.png)

There are total `6` negative numbers.

*Note:* It's easy to solve this problem in **O(N*M)** time, can you do it in **O(N + M)**?

---

## Input Format

- The first line of input contains two space separated integers $N$ and $M$, denoting the no. of rows and columns in input matrix
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, the count of negative integers in the given matrix.

---

## Constraints

- $1 \leq N, m \leq 100$
- The absolute value of the matrix's elements doesn't exceed $100000$.

---

## Examples

**Example 1**

**Input**

```text
3 4
8 7 6 -1
7 7 -1 -2
4 -5 -6 -7
```

**Output**

```text
6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops, Observation.

**Problem:**

Given a `N x M` matrix which is sorted in non-increasing order both row-wise and column-wise, count the number of negative numbers in matrix.

**Solution Approach:**

The simple solution is to just iterate through entire matrix and count the no. of negative numbers in it. That will take O(N * M) time. However since matrix is sorted row/column wise non-increasingly, we can use that to our advantage. Let’s see how:

We start from the top-right corner of the matrix. At each row, we iterate column-wise from right to left until we encounter the first non-negative number. Since the matrix is sorted in non-increasing order, once we find a non-negative number, all the elements to its left in that row will also be non-negative. Therefore, we can determine the count of negative numbers in that row by subtracting the column index of the first negative number from the total number of columns and then subtracting one (to exclude the non-negative number itself). We accumulate this count for each row, and at the end of the traversal, we return the total count of negative numbers in the entire matrix.

**Time Complexity**:  O(N + M), as we traverse from right to left and top to bottom only once, in staircase manner.

**Space Complexity**: O(1).

</details>

# Sum of Diagonals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATDIAGSUM |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATDIAGSUM](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATDIAGSUM) |

---

## Problem Statement

Given a `N x N` square matrix, find the sum of both primary as well as secondary diagonal elements.

For eg. in the following matrix:

![matdiagsum](https://i.ibb.co/GCkbRDz/Screenshot-2024-03-14-at-9-06-17-PM.png)

Sum of primary and secondary diagonal element = 3 + 2 + 0 + 4 + 5 = 14

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the no. of rows and columns in input matrix
- Next $N$ lines contain $N$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, the sum of diagonals elements.

---

## Constraints

- $1 \leq N \leq 100$
- The elements of the matrix are non-negative and won't exceed $1000$.

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
14
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops, Observation.

**Problem:** Given a N x N square matrix, find the sum of both primary as well as secondary diagonal elements.

**Solution Approach:**

We iterate through the rows of the matrix, and for each row, we access the corresponding elements on both diagonals. For the primary diagonal, the row index is equal to the column index, and for the secondary diagonal, the row index is equal to (N - column index - 1), where N is the size of the matrix. We accumulate the values of these elements into a sum variable. If the row index is equal to the column index, we only add the value of the element once to avoid counting it twice for both diagonals. Finally, we return the total sum computed.

**Time Complexity**: O(N) as we just need to iterate through first column.

**Space Complexity**: O(1).

</details>

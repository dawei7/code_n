# Upside Down Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATTREVERSE |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATTREVERSE](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATTREVERSE) |

---

## Problem Statement

Given a `N x M`(N rows and M columns) matrix, print it upside down, i.e, last row should come first, second last should come second......so on..and finally first row should come in last.

See the following example:

![matrotate](https://i.ibb.co/WKP3Fkd/Screenshot-2024-03-14-at-12-05-11-PM.png)

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output $N$ lines contains $M$ space separated integers, the elements of the given matrix in upside down manner.

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
3 1 5
8 2 1
4 6 0
```

**Output**

```text
4 6 0
8 2 1
3 1 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops

**Problem:** Given an N x M matrix, print it upside down, with the last row appearing first, the second-to-last row appearing second, and so on, until the first row appears last.

**Solution Approach:**

We can traverse the matrix in reverse order (from the last row to the first row) and print each row element by element. The print each row followed by a newline character after printing all elements of the row.

**Time Complexity:**

The time complexity of this solution is O(N * M), where N is the number of rows and M is the number of columns in the matrix. This complexity arises from traversing all elements of the matrix.

**Space Complexity:** O(1), as we don’t need any extra space.

</details>

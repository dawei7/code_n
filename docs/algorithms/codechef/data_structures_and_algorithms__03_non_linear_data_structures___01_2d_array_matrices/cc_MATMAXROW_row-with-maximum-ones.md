# Row With Maximum Ones

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMAXROW |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMAXROW](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMAXROW) |

---

## Problem Statement

Find the row with maximum no. of 1’s in a row-wise sorted binary matrix. If there are many such rows, print the first one.

For eg. in the following matrix:

![matmaxrow](https://i.ibb.co/Bcw5c7P/Screenshot-2024-03-14-at-3-19-31-PM.png)

Both row `2` and row `4` has maximum number of 1's, hence the answer would be **2** as its the first row which has maximum 1's.

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the row-wise sorted binary matrix.
- Next $N$ lines contains $N$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line the row number which has maximum 1's.
- **Follow up:** can you solve it in better than `O(N*M)` time complexity?

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are either `0` or `1`.
- Matrix is row-wise sorted.

---

## Examples

**Example 1**

**Input**

```text
3 3
0 1 1
0 1 1
0 1 1
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Binary Search *(for efficient solution).*

**Problem:** Find the row with maximum no. of 1’s in a row-wise sorted binary matrix. If there are many such rows, print the first one.

**Solution Approach:**

We can simply iterate through the matrix keeping track of no. of 1s in each row. Only update the answer when you find a row with larger no. of 1s than that in all previous rows.

An efficient approach would be to use binary search on each row to find no. of 1s in it in *O(logM)* time instead of *O(M)* time

**Time Complexity**:  O(N * M) for simple approach, O(N*log(M)) for more efficient approach.

**Space Complexity**: O(1).

</details>

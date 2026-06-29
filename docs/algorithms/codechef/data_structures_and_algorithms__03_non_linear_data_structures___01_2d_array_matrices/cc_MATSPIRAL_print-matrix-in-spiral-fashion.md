# Print Matrix In Spiral Fashion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATSPIRAL |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATSPIRAL](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATSPIRAL) |

---

## Problem Statement

Given an `N x M` integer matrix, print its element in spiral fashion (clockwise).

See the following example:

![matsetzero](https://i.ibb.co/JBwGmQP/Screenshot-2024-03-14-at-2-03-38-PM.png)

Output should be: 1 2 3 4 8 12 11 10 9 5 6 7

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on $N*M$ space separated integers, the elements of input matrix in spiral fashion.

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are non-negative and won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

**Output**

```text
1 2 3 4 8 12 11 10 9 5 6 7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops.

**Problem:**

Given an N x M integer matrix, print its elements in spiral fashion (clockwise).

**Solution Approach:**

Basically the core idea of the algorithm is to traverse the given matrix in mentioned spiral order carefully such that we don’t print same value more than once.

How to do that? By using loops intelligently.

*Steps:*

- **Initialization**: Initialize variables for the boundaries of the matrix: `left`, `right`, `top`, and `bottom`. Also, initialize a variable `direction` to indicate the direction of traversal.

- **Spiral Traversal**: Traverse the matrix in a spiral fashion, printing elements as per the current direction of traversal.

- If `direction` is 1 (moving from left to right), print the elements in the top row from `left` to `right`, then increment `top`.

- If `direction` is 2 (moving from top to bottom), print the elements in the rightmost column from `top` to `bottom`, then decrement `right`.

- If `direction` is 3 (moving from right to left), print the elements in the bottom row from `right` to `left`, then decrement `bottom`.

- If `direction` is 4 (moving from bottom to top), print the elements in the leftmost column from `bottom` to `top`, then increment `left`.

- **Update Direction**: After traversing in one direction, update the `direction` variable to continue traversal in the next direction.

- **Termination Condition**: Continue the traversal until all elements have been printed (until `left` is less than or equal to `right` and `top` is less than or equal to `bottom`).

- **Output**: Print each element followed by a space character.

**Time Complexity:**

- Let N be the number of rows and M be the number of columns in the matrix.

- Since each element of the matrix is visited exactly once, the time complexity is O(N * M).

**Space Complexity:**

- The space complexity is O(1), as only a few variables are used.

</details>

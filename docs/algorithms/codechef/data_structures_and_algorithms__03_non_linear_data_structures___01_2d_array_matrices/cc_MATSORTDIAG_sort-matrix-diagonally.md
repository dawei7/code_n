# Sort Matrix Diagonally

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATSORTDIAG |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATSORTDIAG](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATSORTDIAG) |

---

## Problem Statement

Given a `N x M` matrix, sort its elements diagonally.
For eg. see the following matrix and its diagonal sorting:

![matsortdiag](https://i.ibb.co/Pr3FXjF/Screenshot-2024-03-16-at-8-24-04-PM.png)

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output $N$ lines, each containing $M$ space separated integers, the elements of diagonally sorted matrix.

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
0 1 5
6 2 1
4 8 3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Loops, Map/Priority Queue.

**Problem:** Given an N x M matrix, sort its elements diagonally.

**Solution Approach:**

The core of the solution is the fact that, *elements on the same diagonal have the same row-column index difference*.

Steps:

- **Initialize Data Structures**: Create a map where the key represents the difference between row and column indices, and the value is a priority queue to store elements on each diagonal.

- **Populate Diagonals**: Traverse the matrix and insert each element into the appropriate diagonal in the map based on its row-column index difference.

- **Sort Diagonals**: Traverse the matrix again and replace each element with the top element of the corresponding diagonal’s priority queue, effectively sorting each diagonal.

- **Output**: print the sorted matrix.

**Time Complexity:**

- Let N be the number of rows and M be the number of columns.

- Populating Diagonals: O(N * M) to traverse all elements of the matrix.

- Sorting Diagonals: O(N * M * log(min(N, M))) to sort each diagonal using priority queues.

- Overall time complexity: O(N * M * log(min(N, M)))

**Space Complexity:**

- Additional space is used to store the map and priority queues.

- Space complexity: O(N * M) for the map and priority queues, and additional constant space for variables used in the program.

</details>

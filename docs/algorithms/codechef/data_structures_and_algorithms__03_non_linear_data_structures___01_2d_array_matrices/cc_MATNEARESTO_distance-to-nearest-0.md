# Distance to Nearest 0

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATNEARESTO |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATNEARESTO](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATNEARESTO) |

---

## Problem Statement

Given is a `N x M` binary matrix, for each cell find its distance from the nearest `0`.

**Note:** Distance between vertically or horizontally adjacent cells is `1`. (See the sample input/output for more clarity)

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the matrix.
- Next $N$ lines containing $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output $N$ lines containing $M$ space separated integers, the distance of each cell from nearest `0`.

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are either `0` or `1`.
- There is at least one `0` in the matrix.

---

## Examples

**Example 1**

**Input**

```text
3 3
0 1 1
0 1 0
1 1 1
```

**Output**

```text
0 1 1
0 1 0
1 2 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, BFS.

**Problem:** Given is a `N x M` binary matrix, for each cell find its distance from the nearest `0`. Distance between vertically or horizontally adjacent cells is `1`.

**Solution Approach:**

We can solve this problem using BFS in the given matrix.

Solution processes the given binary matrix to compute the distance of each cell from the nearest 0. We can initialize a queue to store the positions of cells containing 0s. Then, iterate through each cell of the matrix. If a cell contains a 0, its position is added to the queue, and its value is set to 0. If a cell contains a 1, its value is set to -1, indicating that it needs to be processed. Then inside the BFS loop, we dequeue cells from the queue and examines their neighbors in the four cardinal directions. For each neighboring cell with a value of -1 (indicating it hasn’t been processed), the function updates its value to the distance from the nearest 0 and adds its position to the queue for further processing. This process continues until the queue is empty, and all cells have been processed.

**Time Complexity**: O(N * M), as we might need to process entire matrix in worst case.

**Space Complexity**: O(N * M), as we might need to store entire cells in the BFS queue.

</details>

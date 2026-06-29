# Maximum Area Island

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMAXISLAND |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMAXISLAND](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMAXISLAND) |

---

## Problem Statement

Given is a `N x M` binary matrix which represents islands. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in matrix. If there is no island, return `0`.

For eg., in the following matrix:

![matmaxisland](https://i.ibb.co/5G584d1/Screenshot-2024-03-14-at-4-03-21-PM.png)

Maximum area of island is: **5** (lands are highlighted in maximum area island).

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the matrix.
- Next $N$ lines containing $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line the maximum area of the island.

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are either `0` or `1`.

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
6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, DFS

**Problem:** Given is a `N x M` binary matrix which represents islands. An island is a group of 1’s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in matrix. If there is no island, return `0`.

**Solution Approach:** The main idea is to systematically explore each cell in the binary matrix to identify and calculate the area of islands. Starting from the top-left corner, we traverse the matrix, recursively exploring neighboring cells in all four directions (up, down, left, right) to identify contiguous regions of land (1s). As we traverse each cell, we mark it as water (0) to prevent revisiting during subsequent explorations. The recursive exploration terminates when the boundary of the matrix is reached or when a cell representing water is encountered. By repeating this process for every cell in the matrix, we compute the area of each island. Finally, we track the maximum area among all islands encountered.

**Time Complexity**:  O(N * M)

**Space Complexity**: O(1)

</details>

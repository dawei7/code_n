# Rotting Apples

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATROTAPPLE |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATROTAPPLE](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATROTAPPLE) |

---

## Problem Statement

Given an `N x M` matrix where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh apple, or
- `2` representing a rotten apple.

Every minute, any fresh apple that is `4`-directionally adjacent to a rotten apple becomes rotten.

`4`-directionally adjacent cells of a cell _(i, j)_ are cell _(i - 1, j)_, _(i + 1, j)_, _(i, j - 1)_ and _(i, j + 1)_.

Find the minimum number of minutes that must elapse until no cell has a fresh apple. If this is impossible, return -1.

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, the minimum number of minutes that must elapse until no cell has a fresh apple. If this is impossible, output -1.

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are either `0`, `1` or `2`.

---

## Examples

**Example 1**

**Input**

```text
3 4
0 2 1 1  
1 1 0 1 
1 1 0 1
```

**Output**

```text
4
```

**Explanation**

There is a rotten apple in cell (0, 1) (assuming 0-based indexing).

After 1 minute: fresh apples in cells (0, 2) and (1, 1) gets rotten.

After 2 minutes: fresh apples in cells (0, 3), (1, 0) and (2, 1) gets rotten.

After 3 minutes: fresh apples in cells (2, 0) and (1, 3) gets rotten.

After 4 minutes: the last fresh apple in cell (2, 3) gets rotten.

Hence it takes minimum 4 minutes to rot all apples.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, BFS.

**Problem:**  Given an `N x M` matrix where each cell can have one of three values:

- `0` representing an empty cell,

- `1` representing a fresh apple, or

- `2` representing a rotten apple.

Every minute, any fresh orange that is `4`-directionally adjacent to a rotten apple becomes rotten.

Find the minimum number of minutes that must elapse until no cell has a fresh apple. If this is impossible, return -1.

**Solution Approach:**

The core idea of the solution is to simulate the process of rotting apples in a grid. We start by initializing a queue to store the positions of rotten apples and counting the number of fresh apples in the grid. Then, in each iteration, we process all currently rotten apples by checking their adjacent cells. If a fresh apple is found adjacent to a rotten apple, it becomes rotten in the next minute, and we enqueue its position for further processing. This process continues until no fresh apples are left or until all reachable fresh apples have become rotten. Throughout the simulation, we track the number of minutes elapsed. If all fresh apples have been rotten after the simulation, we return the total number of minutes. Otherwise, if there are still fresh apples remaining but no more reachable rotten apples, it indicates that some fresh apples are unreachable and will never rot, so we return -1 to indicate that it’s impossible for all fresh apples to become rotten.

**Time Complexity**:   O(N * M), where N is the number of rows and M is the number of columns in the grid. This is because we traverse each cell in the grid once during the initialization and the simulation process.

**Space Complexity**: O(N * M). This is primarily due to the usage of the queue to store the positions of rotten apples, which can potentially hold up to all the cells in the grid

</details>

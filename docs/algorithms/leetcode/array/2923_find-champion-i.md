# Find Champion I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2923 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [find-champion-i](https://leetcode.com/problems/find-champion-i/) |

## Problem Description & Examples
### Goal
Given a square adjacency matrix representing the results of matches between $n$ teams, identify the "champion." A team is the champion if it has defeated every other team in the tournament. The matrix `grid[i][j] == 1` indicates team `i` defeated team `j`, while `grid[i][j] == 0` indicates the opposite (where `i != j`). It is guaranteed that exactly one champion exists.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (a square $n \times n$ matrix) where `grid[i][j]` is 1 if team `i` beat team `j`, and 0 otherwise.

**Return value**

- An integer representing the index of the team that has defeated all other teams.

### Examples
**Example 1**

- Input: `grid = [[0,1],[0,0]]`
- Output: `0`

**Example 2**

- Input: `grid = [[0,0,1],[1,0,1],[0,0,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[0,0,0],[1,0,0],[1,1,0]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem can be solved by identifying the row in the matrix that contains only 1s (excluding the diagonal). Since the problem guarantees a unique champion, we are looking for the row index `i` such that the sum of the row is equal to $n-1$. Alternatively, one can perform a linear scan to find the team that never lost a match (i.e., the column index `j` where no `1` exists in that column).

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the number of teams, as we must inspect the entries of the $n \times n$ matrix.
- **Space Complexity**: $O(1)$, as we only store a few variables to track the current candidate or row sums, regardless of the input size.

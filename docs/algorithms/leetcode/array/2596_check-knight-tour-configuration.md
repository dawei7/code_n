# Check Knight Tour Configuration

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2596 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Simulation |
| Official Link | [check-knight-tour-configuration](https://leetcode.com/problems/check-knight-tour-configuration/) |

## Problem Description & Examples
### Goal
Given an $n \times n$ grid representing a sequence of moves made by a knight on a chessboard, determine if the sequence forms a valid knight's tour. A valid tour must start at the top-left corner (0, 0) with the value 0, and each subsequent move must follow the standard L-shaped movement pattern of a knight, visiting every cell from 0 to $n^2 - 1$ exactly once.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size $n \times n$ representing the order in which cells were visited.

**Return value**

- `bool`: Returns `True` if the provided grid represents a valid knight's tour, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]`
- Output: `True`

**Example 2**

- Input: `grid = [[0,3,6],[5,8,1],[2,7,4]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem is solved using **Simulation**. Since the grid contains exactly one instance of every number from $0$ to $n^2 - 1$, we can map each value to its coordinate $(r, c)$. We then iterate through the sequence from $0$ to $n^2 - 1$ and verify that the distance between the coordinates of step $i$ and step $i+1$ satisfies the knight's move condition: $|r_1 - r_2| \times |c_1 - c_2| = 2$ (specifically, the set of absolute differences must be $\{1, 2\}$).

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the grid. We traverse the grid once to map the positions and once to validate the moves.
- **Space Complexity**: $O(n^2)$ to store the mapping of each step value to its $(r, c)$ coordinate.

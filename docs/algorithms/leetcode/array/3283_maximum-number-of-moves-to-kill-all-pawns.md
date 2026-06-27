# Maximum Number of Moves to Kill All Pawns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3283 |
| Difficulty | Hard |
| Topics | Array, Math, Bit Manipulation, Breadth-First Search, Game Theory, Bitmask |
| Official Link | [maximum-number-of-moves-to-kill-all-pawns](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/) |

## Problem Description & Examples
### Goal
Given a knight's starting position on a chessboard and a list of target pawns, determine the total number of moves made in a game where Alice and Bob take turns moving the knight. Alice aims to maximize the total number of moves until all pawns are captured, while Bob aims to minimize it. Each turn, the current player moves the knight to capture a remaining pawn, and the game ends when no pawns are left.

### Function Contract
**Inputs**

- `kx`: An integer representing the starting row of the knight.
- `ky`: An integer representing the starting column of the knight.
- `positions`: A list of lists, where each sub-list `[px, py]` represents the coordinates of a pawn.

**Return value**

- An integer representing the total number of moves made in the game assuming optimal play from both sides.

### Examples
**Example 1**

- Input: `kx = 1, ky = 1, positions = [[0, 0]]`
- Output: `4`

**Example 2**

- Input: `kx = 0, ky = 2, positions = [[1, 1], [2, 2], [3, 3]]`
- Output: `8`

**Example 3**

- Input: `kx = 0, ky = 0, positions = [[1, 2], [2, 4]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of Breadth-First Search (BFS) to precompute the shortest distance between all pairs of points (start position and all pawns), followed by Minimax with Memoization (Dynamic Programming with Bitmasking) to determine the optimal game outcome.

---

## Complexity Analysis
- **Time Complexity**: $O(N^2 + 2^N \cdot N^2)$, where $N$ is the number of pawns. The BFS takes $O(N \cdot 50^2)$ and the DP state space is $2^N \cdot N$.
- **Space Complexity**: $O(N^2 + 2^N \cdot N)$ to store the distance matrix and the memoization table.

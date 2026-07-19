# Sliding Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 773 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Breadth-First Search, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-puzzle/) |

## Problem Description

### Goal

Given a $2 x 3$ board containing each value from `0` through `5` exactly once, value `0` represents the blank square. In one move, swap the blank with one horizontally or vertically adjacent tile.

Return the minimum number of moves needed to reach the solved board `[[1,2,3],[4,5,0]]`. If no sequence of legal swaps can reach that arrangement, return `-1`. The other tiles cannot move except by swapping with the current blank position.

### Function Contract

**Inputs**

- `board`: a $2 x 3$ permutation of the integers `0` through `5`.

**Return value**

- The shortest legal move count to the target board, or `-1` when no legal sequence exists.

### Examples

**Example 1**

- Input: `board = [[1,2,3],[4,0,5]]`
- Output: `1`
- Explanation: Swap the blank with tile `5`.

**Example 2**

- Input: `board = [[1,2,3],[5,4,0]]`
- Output: `-1`
- Explanation: This permutation has the wrong parity and cannot reach the target.

**Example 3**

- Input: `board = [[4,1,2],[5,0,3]]`
- Output: `5`
- Explanation: The shortest legal sequence contains five blank swaps.

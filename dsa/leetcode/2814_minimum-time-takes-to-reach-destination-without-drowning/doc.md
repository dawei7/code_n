# Minimum Time Takes to Reach Destination Without Drowning

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2814 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/) |

## Problem Description

### Goal

You stand at the unique `S` cell of a rectangular grid and want to reach the unique destination `D`. Empty cells are `.`, stones are `X`, and initially flooded cells are `*`. Each second you may move one cell orthogonally, while flooding simultaneously spreads from every flooded cell into adjacent empty cells.

You may never enter a stone or flooded cell. A move is also invalid when its destination becomes flooded during that same second. The destination never floods. Return the fewest seconds needed to reach `D`, or `-1` when every possible journey is blocked or overtaken by water.

### Function Contract

**Inputs**

- `land`: An $r\times c$ matrix of `"S"`, `"D"`, `"."`, `"*"`, and `"X"`, with $2 \leq r,c \leq 100$ and exactly one start and destination.

Let $N=rc$ be the number of cells.

**Return value**

Return the minimum safe arrival time at `D`, or `-1` if no safe path exists.

### Examples

**Example 1**

- Input: `land = [["D",".","*"],[".",".","."],[".","S","."]]`
- Output: `3`
- Explanation: A three-step route reaches the destination before flooding enters any cell used at the same time.

**Example 2**

- Input: `land = [["D","X","*"],[".",".","."],[".",".","S"]]`
- Output: `-1`
- Explanation: Every route to the destination is overtaken before its minimum four-step travel time.

**Example 3**

- Input: `land = [["D",".",".",".","*","."],[".","X",".","X",".","."],[".",".",".",".","S","."]]`
- Output: `6`
- Explanation: A safe route exists and its shortest travel time is six seconds.

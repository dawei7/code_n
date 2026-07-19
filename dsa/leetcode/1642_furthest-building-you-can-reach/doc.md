# Furthest Building You Can Reach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1642 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/furthest-building-you-can-reach/) |

## Problem Description
### Goal
An array `heights` gives the heights of consecutive buildings. Starting at building 0, move from each building `i` to `i + 1` while using a limited supply of bricks and ladders.

Moving to an equal or lower building costs nothing. For a positive climb of `heights[i + 1] - heights[i]`, either spend exactly that many bricks or use one ladder. Return the largest 0-indexed building position reachable when the resources are assigned optimally.

### Function Contract
**Inputs**

- `heights`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{heights[i]} \le 10^6$.
- `bricks`: the available brick count, where $0 \le \texttt{bricks} \le 10^9$.
- `ladders`: the available ladder count, where $0 \le \texttt{ladders} \le n$.

**Return value**

Return the furthest building index reachable by moving only to the next building and assigning bricks or ladders to every positive climb.

### Examples
**Example 1**

- Input: `heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1`
- Output: `4`

Spending five bricks on the climb from 2 to 7 and the ladder on the climb from 6 to 9 reaches building 4, but the later climb cannot be paid.

**Example 2**

- Input: `heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2`
- Output: `7`

**Example 3**

- Input: `heights = [14,3,19,3], bricks = 17, ladders = 0`
- Output: `3`

The only positive climb costs 16 bricks.

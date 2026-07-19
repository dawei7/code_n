# Minimum Sideway Jumps

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-sideway-jumps/) |
| Frontend ID | 1824 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A road has three lanes and points numbered from 0 through $n$. A frog begins at point 0 in lane 2 and wants to reach point $n$ in any lane. At each point there is either no obstacle or one obstacle blocking exactly the lane recorded by `obstacles[i]`; value 0 means no lane is blocked.

The frog may advance from point $i$ to $i+1$ in its current lane when the destination is unblocked. It may also side-jump at one point to either other lane, including the nonadjacent lane, provided the destination lane is unblocked there. Points 0 and $n$ are obstacle-free. Return the fewest side jumps required.

### Function Contract

**Inputs**

- `obstacles`: an array of length $n+1$, where $1 \le n \le 5\cdot10^5$.
- Each value is from 0 through 3; a nonzero value names the single blocked lane at that point.
- `obstacles[0] = obstacles[n] = 0`.

**Return value**

- Return the minimum number of side jumps needed to reach point $n$ in any lane from lane 2 at point 0.

### Examples

**Example 1**

- Input: `obstacles = [0,1,2,3,0]`
- Output: `2`

**Example 2**

- Input: `obstacles = [0,1,1,3,3,0]`
- Output: `0`

Lane 2 remains clear throughout, so forward movement alone reaches the end.

**Example 3**

- Input: `obstacles = [0,2,1,0,3,0]`
- Output: `2`

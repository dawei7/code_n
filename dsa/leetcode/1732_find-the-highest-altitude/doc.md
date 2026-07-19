# Find the Highest Altitude

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1732 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/) |

## Problem Description

### Goal

A biker travels through $n + 1$ points whose altitudes may differ. Point $0$ is the start of the trip and has altitude $0$.

The length-$n$ integer array `gain` describes the route: `gain[i]` is the net altitude change from point $i$ to point $i + 1$. Apply these changes in route order and return the highest altitude attained at any point, including the initial altitude of $0$.

### Function Contract

**Inputs**

- `gain`: an integer list of length $n$, where `gain[i]` is the net altitude change along one route segment.
- The contract guarantees $1 \le n \le 100$ and $-100 \le \texttt{gain[i]} \le 100$.

**Return value**

- Return the maximum altitude among all $n + 1$ route points, with the starting altitude included.

### Examples

**Example 1**

- Input: `gain = [-5,1,5,0,-7]`
- Output: `1`
- Explanation: The point altitudes are `0,-5,-4,1,1,-6`, whose maximum is $1$.

**Example 2**

- Input: `gain = [-4,-3,-2,-1,4,3,2]`
- Output: `0`
- Explanation: Every later altitude is below the initial altitude.

**Example 3**

- Input: `gain = [3,-1,2,-2]`
- Output: `4`
- Explanation: The altitudes are `0,3,2,4,2`, so the peak occurs before the trip ends.

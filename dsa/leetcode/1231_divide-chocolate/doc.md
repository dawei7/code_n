# Divide Chocolate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1231 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-chocolate/) |

## Problem Description

### Goal

A chocolate bar consists of consecutive chunks, and `sweetness[i]` gives the sweetness of the $i$th chunk. You want to share the bar with `k` friends by making exactly `k` cuts. Every cut lies between two adjacent chunks, so the cuts divide the bar into `k + 1` nonempty contiguous pieces.

After giving one piece to each friend, you keep the remaining piece. You act as generously as possible: among all valid placements of the cuts, maximize the minimum total sweetness of any piece. Return that greatest achievable minimum, which is the amount of sweetness you can guarantee for the piece you keep.

### Function Contract

**Inputs**

- `sweetness`: A list of $n$ positive chunk sweetness values, where $1\le n\le10^4$ and $1\le\texttt{sweetness[i]}\le10^5$.
- `k`: The exact number of cuts, where $0\le k<n$; the bar is divided into `k + 1` pieces.

Define the total sweetness as

$$
S = \sum_{i=0}^{n-1} \texttt{sweetness[i]}.
$$

**Return value**

- The maximum possible minimum total sweetness among the `k + 1` contiguous pieces.

### Examples

**Example 1**

- Input: `sweetness = [1,2,3,4,5,6,7,8,9]`, `k = 5`
- Output: `6`

Six pieces can all reach sweetness $6$, but requiring every piece to reach $7$ is impossible.

**Example 2**

- Input: `sweetness = [5,6,7,8,9,1,2,3,4]`, `k = 8`
- Output: `1`

Eight cuts make every chunk its own piece, so the least-sweet chunk determines the answer.

**Example 3**

- Input: `sweetness = [1,2,2,1,2,2,1,2,2]`, `k = 2`
- Output: `5`

Cutting after each group `[1,2,2]` produces three pieces of sweetness $5$.

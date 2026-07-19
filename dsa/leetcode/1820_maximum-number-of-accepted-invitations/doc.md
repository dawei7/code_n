# Maximum Number of Accepted Invitations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) |
| Frontend ID | 1820 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A party has $m$ boys and $n$ girls. The binary matrix `grid` describes which invitations can be accepted: `grid[i][j] = 1` means boy `i` may invite girl `j` and she would accept, while zero means that pairing is unavailable.

Each boy may send an invitation to at most one girl, and each girl may accept an invitation from at most one boy. Choose compatible boy-girl pairs subject to both exclusivity rules and return the greatest number of invitations that can be accepted simultaneously.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ binary matrix, where $1 \le m,n \le 200$.
- `grid[i][j]` is 1 exactly when the edge from boy `i` to girl `j` is available.

**Return value**

- Return the maximum number of pairwise non-conflicting available boy-girl matches.

### Examples

**Example 1**

- Input: `grid = [[1,1,1],[1,0,1],[0,0,1]]`
- Output: `3`

All three boys can be paired with different acceptable girls.

**Example 2**

- Input: `grid = [[1,0,1,0],[1,0,0,0],[0,0,1,0],[1,1,1,0]]`
- Output: `3`

The fourth girl has no incident edge, but three non-conflicting invitations can still be accepted.

# Find Champion I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2923 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-champion-i/) |

## Problem Description

### Goal

A tournament contains $n$ teams numbered from 0 through $n-1$. The 0-indexed
$n\times n$ boolean matrix `grid` describes their relative strength: for
distinct teams $i$ and $j$, `grid[i][j] == 1` means team $i$ is stronger
than team $j$; otherwise team $j$ is stronger than team $i$.

The relation is complete and transitive, and every diagonal entry is zero. A
team is the champion when no other team is stronger than it. Return that
team's index.

### Function Contract

**Inputs**

- `grid`: A square boolean matrix encoding every pairwise strength
  comparison.

Let $n=\lvert\texttt{grid}\rvert$. The constraints are $2\le n\le100$.
Every entry is 0 or 1, `grid[i][i] == 0`, opposite off-diagonal entries
differ, and the represented strength relation is transitive.

**Return value**

- The index of the tournament champion.

### Examples

#### Example 1

- **Input:** `grid = [[0, 1], [0, 0]]`
- **Output:** `0`
- **Explanation:** Team 0 is stronger than team 1, so nobody is stronger than
  team 0.

#### Example 2

- **Input:** `grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]`
- **Output:** `1`
- **Explanation:** Team 1 is stronger than both teams 0 and 2.

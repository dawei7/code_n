# Find the Number of Winning Players

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3238 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-winning-players/) |

## Problem Description

### Goal

A game has `n` players numbered from $0$ through $n-1$. Each pair `[x_i, y_i]` in `pick` records that player $x_i$ picked one ball of color $y_i$.

Player $i$ wins when they have picked strictly more than $i$ balls of at least one single color. Counts from different colors cannot be combined, and a player who satisfies the condition for several colors is still counted only once. Return the total number of winning players.

### Function Contract

**Inputs**

- `n`: The player count, with $2\leq\texttt{n}\leq10$.
- `pick`: Between $1$ and $100$ pairs `[player, color]`, where player identifiers lie in $[0,n-1]$ and colors lie in $[0,10]$.

Let $p=\lvert\texttt{pick}\rvert$.

**Return value**

Return the number of distinct players who have at least $i+1$ picks of one color.

### Examples

**Example 1**

- Input: `n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]`
- Output: `2`
- Explanation: Players $0$ and $1$ win; player $2$ has three picks split across two colors.

**Example 2**

- Input: `n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]`
- Output: `0`
- Explanation: Player $1$ never picks the same color twice.

**Example 3**

- Input: `n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]`
- Output: `1`
- Explanation: Player $2$ picks color $4$ three times.

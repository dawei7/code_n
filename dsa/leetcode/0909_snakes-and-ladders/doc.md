# Snakes and Ladders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 909 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/snakes-and-ladders/) |

## Problem Description
### Goal
An $n\times n$ board has squares labeled from $1$ through $n^2$ in Boustrophedon order: labeling begins at `board[n - 1][0]` in the bottom-left corner, proceeds left to right across that row, and reverses horizontal direction on every row above it. You start on square $1$.

From a current square `curr`, one dice roll lets you choose any square `next` from `curr + 1` through $\min(\texttt{curr}+6,n^2)$. If that square starts a snake or ladder, you must move to its recorded destination; otherwise you remain on `next`. Apply at most one snake or ladder per roll, even when its destination starts another transition. The game ends upon reaching square $n^2$.

Return the least number of dice rolls needed to reach the final square. Return $-1$ when no sequence of rolls can reach it.

### Function Contract
Let $n=\lvert\texttt{board}\rvert$.

**Inputs**

- `board`: an $n\times n$ integer matrix with $2 \leq n \leq 20$. Each cell is $-1$ or a destination label in $[1,n^2]$. A value other than $-1$ marks the start of a snake or ladder. Squares $1$ and $n^2$ do not start transitions.

**Return value**

Return the minimum number of rolls required to reach square $n^2$, or $-1$ if it is unreachable.

### Examples
**Example 1**

- Input: `board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]`
- Output: `4`

One optimal route uses the transitions $2\to15$, $17\to13$, and $14\to35$, then reaches square $36$.

**Example 2**

- Input: `board = [[-1,-1],[-1,3]]`
- Output: `1`

The final square is reachable with one roll.

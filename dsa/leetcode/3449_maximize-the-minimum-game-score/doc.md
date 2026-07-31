# Maximize the Minimum Game Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3449 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-minimum-game-score/) |

## Problem Description
### Goal
An array `points` describes a game board with one score value per index. A separate array `gameScore` of the same length starts with every entry equal to zero, while the player starts just to the left of the board at index $-1$.

The player may make at most `m` moves. A move changes the current index by exactly one, either left or right; staying in place is not a move option. After the first move, the current index must always lie between $0$ and $n-1$. Whenever the player arrives at index $i$, `points[i]` is added to `gameScore[i]`. Choose the moves so that the minimum value in `gameScore` is as large as possible, and return that maximum value.

### Function Contract
**Inputs**

- `points`: A list of $n$ positive integers, where `points[i]` is added on every visit to index $i$.
- `m`: The maximum number of moves available.

The constraints are $2 \le n \le 5 \cdot 10^4$, $1 \le \texttt{points[i]} \le 10^6$, and $1 \le m \le 10^9$.

For complexity notation, let $p = \min_i \texttt{points[i]}$.

**Return value**

Return the greatest achievable value of $\min_i \texttt{gameScore[i]}$ after making at most `m` moves.

### Examples
**Example 1**

- Input: `points = [2, 4], m = 3`
- Output: `4`

**Example 2**

- Input: `points = [1, 2, 3], m = 5`
- Output: `2`

**Example 3**

- Input: `points = [7, 2, 9, 3], m = 3`
- Output: `0`

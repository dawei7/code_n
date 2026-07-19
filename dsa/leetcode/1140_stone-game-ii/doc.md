# Stone Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1140 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Prefix Sum, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/stone-game-ii/) |

## Problem Description

### Goal

Alice and Bob play with a row of piles, where `piles[i]` is the positive number of stones in pile `i`. Alice moves first, and both players choose moves optimally with the objective of finishing with as many stones as possible.

Initially, `M = 1`. On a turn, the player chooses an integer `X` with $1 \le X \le 2M$ and takes every stone from the first `X` remaining piles. The shared parameter is then updated with `M = max(M, X)`. Turns continue until no piles remain. Return the maximum number of stones Alice can obtain.

### Function Contract

**Inputs**

- `piles`: an array of $n$ positive pile sizes, where $1 \le n \le 100$.
- Every `piles[i]` satisfies $1 \le \texttt{piles[i]} \le 10^4$.

**Return value**

The maximum total number of stones Alice can collect when both Alice and Bob play optimally.

### Examples

**Example 1**

- Input: `piles = [2, 7, 9, 4, 4]`
- Output: `10`
- Explanation: Taking one pile first lets Bob take two, after which Alice can take the final two and collect `2 + 4 + 4 = 10`. Taking two initially gives Alice only `9` because Bob can then take all remaining piles.

**Example 2**

- Input: `piles = [1, 2, 3, 4, 5, 100]`
- Output: `104`

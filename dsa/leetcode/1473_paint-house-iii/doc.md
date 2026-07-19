# Paint House III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1473 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house-iii/) |

## Problem Description
### Goal

A row contains $m$ houses, and every house must ultimately have one of $n$ colors labeled from $1$ through $n$. A house whose entry in `houses` is nonzero was painted previously and must keep that color. An entry equal to zero is unpainted; assigning it color $c$ costs `cost[i][c - 1]`. The cost matrix still contains rows for previously painted houses, but those values are irrelevant because such houses cannot be repainted.

A neighborhood is a maximal contiguous group of houses sharing one color. For example, `[1,2,2,3,3,2,1,1]` contains the five neighborhoods `[1]`, `[2,2]`, `[3,3]`, `[2]`, and `[1,1]`. Paint every unpainted house so that the finished row contains exactly `target` neighborhoods and the total paid cost is as small as possible. Return `-1` when no legal completion has exactly that neighborhood count.

### Function Contract
**Inputs**

Let $m$ be the house count, $n$ the color count, and $t=\texttt{target}$.

- `houses`: an integer array of length $m$, where `0` denotes an unpainted house and values in $[1,n]$ are immutable colors.
- `cost`: an $m\times n$ matrix; `cost[i][c - 1]` is the price of assigning color $c$ to an unpainted house at index `i`.
- `m`: the row length, where $1 \le m \le 100$.
- `n`: the number of available colors, where $1 \le n \le 20$.
- `target`: the exact required neighborhood count, where $1 \le t \le m$.
- Every painting price lies in $[1,10^4]$.

**Return value**

Return the minimum sum of costs paid for houses that were initially unpainted among all completions with exactly $t$ neighborhoods. Return `-1` if no such completion exists.

### Examples
**Example 1**

- Input: `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `9`
- Explanation: Coloring the row `[1,2,2,1,1]` creates three neighborhoods and costs `1 + 1 + 1 + 1 + 5 = 9`.

**Example 2**

- Input: `houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `11`
- Explanation: Only the first and last houses may change. Choosing `[2,2,1,2,2]` costs `10 + 1 = 11` and forms exactly three neighborhoods.

**Example 3**

- Input: `houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3`
- Output: `-1`
- Explanation: The fixed row already has four neighborhoods, and repainting is forbidden.

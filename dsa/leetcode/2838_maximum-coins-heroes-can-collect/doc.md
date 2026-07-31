# Maximum Coins Heroes Can Collect

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2838 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-coins-heroes-can-collect/) |

## Problem Description
### Goal

A battle contains $n$ heroes and $m$ monsters. The positive integer `heroes[i]` is hero $i$'s power, while `monsters[j]` is monster $j$'s power. A hero can defeat a monster exactly when the monster's power is at most the hero's power.

Defeating monster $j$ awards `coins[j]` coins. A hero's health is not reduced by fighting, so that hero may defeat every monster they are powerful enough to beat. Different heroes may each defeat the same monster, but an individual hero receives that monster's reward only once. Return one total for every hero, preserving the heroes' original order, where each total is the maximum number of coins that hero can collect.

### Function Contract
**Inputs**

- `heroes`: A list of $n$ positive hero powers, where $1 \le n \le 10^5$ and $1 \le \texttt{heroes[i]} \le 10^9$.
- `monsters`: A list of $m$ positive monster powers, where $1 \le m \le 10^5$ and $1 \le \texttt{monsters[j]} \le 10^9$.
- `coins`: A list of $m$ positive rewards aligned with `monsters`, where `coins[j]` belongs to monster $j$ and $1 \le \texttt{coins[j]} \le 10^9$.

The arrays `monsters` and `coins` have equal length $m$.

**Return value**

Return a list `ans` of length $n$ such that `ans[i]` is the sum of `coins[j]` over every index $j$ satisfying $\texttt{monsters[j]} \le \texttt{heroes[i]}$.

### Examples
**Example 1**

- Input: `heroes = [1, 4, 2], monsters = [1, 1, 5, 2, 3], coins = [2, 3, 4, 5, 6]`
- Output: `[5, 16, 10]`
- Explanation: The three heroes can defeat monsters with powers at most $1$, $4$, and $2$, collecting $5$, $16$, and $10$ coins respectively.

**Example 2**

- Input: `heroes = [5], monsters = [2, 3, 1, 2], coins = [10, 6, 5, 2]`
- Output: `[23]`
- Explanation: The hero can defeat all four monsters and therefore collects every reward.

**Example 3**

- Input: `heroes = [4, 4], monsters = [5, 7, 8], coins = [1, 1, 1]`
- Output: `[0, 0]`
- Explanation: Every monster is stronger than either hero.

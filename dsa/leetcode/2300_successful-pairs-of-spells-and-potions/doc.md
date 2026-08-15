# Successful Pairs of Spells and Potions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2300 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/) |

## Problem Description

### Goal

The positive integer arrays `spells` and `potions` describe the strengths of
$n$ spells and $m$ potions. Pairing spell `spells[i]` with potion
`potions[j]` is successful when their product is at least `success`.

For every spell in its original order, count how many potions form a
successful pair. Potions are considered independently for each spell and may
contribute to several output counts.

Return the $n$ counts aligned with `spells`.

### Function Contract

**Inputs**

- `spells`: An array of $n$ positive spell strengths.
- `potions`: An array of $m$ positive potion strengths.
- `success`: The inclusive minimum product for a successful pair.

The contract guarantees $1 \le n,m \le 10^5$, each strength is from 1 through
$10^5$, and $1 \le \texttt{success} \le 10^{10}$.

**Return value**

An integer array where position $i$ contains the number of potions $p$ for
which $\texttt{spells}[i]\cdot p \ge \texttt{success}$.

### Examples

#### Example 1

- **Input:** `spells = [5, 1, 3]`, `potions = [1, 2, 3, 4, 5]`, `success = 7`
- **Output:** `[4, 0, 3]`

#### Example 2

- **Input:** `spells = [3, 1, 2]`, `potions = [8, 5, 8]`, `success = 16`
- **Output:** `[2, 0, 2]`

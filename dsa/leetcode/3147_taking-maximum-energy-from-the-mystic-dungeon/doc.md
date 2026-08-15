# Taking Maximum Energy From the Mystic Dungeon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3147 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/) |

## Problem Description

### Goal

In a mystic dungeon, $n$ magicians stand in a line. The integer at each position of `energy` is the energy obtained from that magician; a negative value means that the encounter takes energy away instead. Choose any magician as the starting point and absorb that magician's energy.

A curse then transports you from index `i` directly to index `i + k`. Continue making jumps of exactly `k` positions until the next destination no longer exists. Every reached magician is mandatory, so a negative value along the route cannot be skipped. Return the maximum total energy obtainable over all valid starting indices.

### Function Contract

**Inputs**

- `energy`: A list of $n$ integers, where $1 \le n \le 10^5$ and $-1000 \le \texttt{energy[i]} \le 1000$.
- `k`: The fixed forward jump distance, with $1 \le k \le n-1$.

**Return value**

Return the greatest total energy among the forced jump paths starting at every index.

### Examples

#### Example 1

- **Input:** `energy = [5, 2, -10, -5, 1], k = 3`
- **Output:** `3`
- **Explanation:** Starting at index `1` visits energies `2` and `1`, for a total of `3`.

#### Example 2

- **Input:** `energy = [-2, -3, -1], k = 2`
- **Output:** `-1`
- **Explanation:** Starting at index `2` gives `-1`, which is better than every other forced path.

#### Example 3

- **Input:** `energy = [10, -3, -20, -4, -5], k = 2`
- **Output:** `-4`
- **Explanation:** Starting at index `0` must continue through `-20` and `-5`, so the best choice is the one-element path from index `3`.

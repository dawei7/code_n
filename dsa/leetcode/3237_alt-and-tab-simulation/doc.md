# Alt and Tab Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3237 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alt-and-tab-simulation/) |

## Problem Description

### Goal

There are $n$ open windows numbered from $1$ through $n$. The permutation `windows` gives their initial front-to-back order: its first entry is on top and its last entry is at the bottom.

Process `queries` from left to right. Each query names a window and moves that window to the top, preserving the relative order of every other window. Repeatedly selecting the window already on top leaves the order unchanged. Return the complete final front-to-back ordering after all queries.

### Function Contract

**Inputs**

- `windows`: A permutation of $[1,n]$, where $1\leq n\leq10^5$.
- `queries`: Between $1$ and $10^5$ window identifiers, each in $[1,n]$.

Let $q=\lvert\texttt{queries}\rvert$.

**Return value**

Return the final permutation after applying every move-to-front query.

### Examples

**Example 1**

- Input: `windows = [1, 2, 3]`, `queries = [3, 3, 2]`
- Output: `[2, 3, 1]`
- Explanation: The orders become `[3, 1, 2]`, `[3, 1, 2]`, and finally `[2, 3, 1]`.

**Example 2**

- Input: `windows = [1, 4, 2, 3]`, `queries = [4, 1, 3]`
- Output: `[3, 1, 4, 2]`
- Explanation: The most recently queried distinct window is `3`, followed by `1` and `4`.

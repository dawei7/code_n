# Minimum Number of Coins to be Added

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2952 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/) |

## Problem Description

### Goal

You are given a 0-indexed array `coins` containing the values of the available
coins and a positive integer `target`. An integer is obtainable when some
nonempty subsequence of the array has that sum. Each coin occurrence may be
selected at most once, and deleting elements to form a subsequence does not
change the relative order of those retained.

You may add coins of any positive values to the array. Determine the minimum
number of added coins needed so that every integer in the inclusive range
$[1,\texttt{target}]$ is obtainable from the resulting collection.

### Function Contract

**Inputs**

- `coins`: the positive values of the currently available coins
- `target`: the inclusive upper endpoint of the sums that all must be obtainable

Let $N=\lvert\texttt{coins}\rvert$. The contract guarantees
$1\le N\le10^5$, $1\le\texttt{target}\le10^5$, and
$1\le\texttt{coins[i]}\le\texttt{target}$.

**Return value**

The minimum count of additional coins required to make every sum from `1`
through `target` obtainable.

### Examples

#### Example 1

- **Input:** `coins = [1,4,10], target = 19`
- **Output:** `2`
- **Explanation:** Adding coins `2` and `8` makes every required sum obtainable.

#### Example 2

- **Input:** `coins = [1,4,10,5,7,19], target = 19`
- **Output:** `1`
- **Explanation:** Adding only coin `2` closes the first gap and the existing coins cover the rest.

#### Example 3

- **Input:** `coins = [1,1,1], target = 20`
- **Output:** `3`
- **Explanation:** Coins `4`, `8`, and `16` are sufficient, and fewer additions cannot cover the whole range.

# Maximum Value of K Coins From Piles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2218 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) |

## Problem Description
### Goal

There are $n$ nonempty piles of coins. Every coin has a positive value, and each inner list `piles[i]` describes one pile from top to bottom.

In one move, you may remove the top coin from any pile and add its value to your wallet. Choose exactly `k` coins across all piles, respecting this top-to-bottom access rule, and return the maximum total value obtainable.

### Function Contract
**Inputs**

- `piles`: A nonempty list of nonempty coin-value lists, each ordered from top to bottom.
- `k`: A positive integer no greater than the total number of coins.

Let

$$
C=\sum_{p\in\texttt{piles}}\lvert p\rvert.
$$

**Return value**

Return the maximum sum achievable by removing exactly `k` coins through legal top-of-pile moves.

### Examples
**Example 1**

- Input: `piles = [[1, 100, 3], [7, 8, 9]], k = 2`
- Output: `101`

**Example 2**

- Input: `piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k = 7`
- Output: `706`

**Example 3**

- Input: `piles = [[5, 4], [3]], k = 1`
- Output: `5`

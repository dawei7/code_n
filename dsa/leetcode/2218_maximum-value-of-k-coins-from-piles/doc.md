# Maximum Value of K Coins From Piles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2218 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-value-of-k-coins-from-piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/).

### Goal
Take exactly `k` coins from several stacks to maximize total value. A coin may only be taken from the top of its stack, and each pile is listed from top to bottom.

### Function Contract
**Inputs**

- `piles`: lists of coin values ordered top-first.
- `k`: the exact total number of coins to take.

**Return value**

The maximum obtainable value.

### Examples
**Example 1**

- Input: `piles = [[1, 100, 3], [7, 8, 9]]`, `k = 2`
- Output: `101`

**Example 2**

- Input: `piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]`, `k = 7`
- Output: `706`

**Example 3**

- Input: `piles = [[5, 4], [3]]`, `k = 1`
- Output: `5`

---

## Solution
### Approach
Use knapsack dynamic programming over piles. Precompute each pile's prefix sums. When processing a pile, for every total coin count try taking `x` coins from that pile and combine its prefix value with the best result for the remaining count from earlier piles.

### Complexity Analysis
- **Time Complexity**: `O(k * C)`, where `C` is the total number of coins considered across all pile prefixes
- **Space Complexity**: `O(k)` with rolling dynamic programming

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

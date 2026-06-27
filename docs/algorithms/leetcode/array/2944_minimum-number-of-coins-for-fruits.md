# Minimum Number of Coins for Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2944 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Official Link | [minimum-number-of-coins-for-fruits](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/) |

## Problem Description & Examples
### Goal
Given an array of fruit prices where the $i$-th fruit costs `prices[i]`, purchasing the $i$-th fruit allows you to acquire the next $i+1$ fruits for free. Determine the minimum total cost required to acquire all $n$ fruits, indexed from 1 to $n$.

### Function Contract
**Inputs**

- `prices`: A list of integers where `prices[i]` represents the cost of the fruit at index `i` (0-indexed).

**Return value**

- An integer representing the minimum cost to collect all fruits.

### Examples
**Example 1**

- Input: `prices = [3, 1, 2]`
- Output: `4`

**Example 2**

- Input: `prices = [1, 10, 1, 1]`
- Output: `2`

**Example 3**

- Input: `prices = [26, 18, 6, 12, 49, 7, 45, 45]`
- Output: `39`

---

## Underlying Base Algorithm(s)
Dynamic Programming with a Monotonic Queue (or Sliding Window Minimum). The state `dp[i]` represents the minimum cost to acquire all fruits up to index `i`. The transition is `dp[i] = prices[i-1] + min(dp[j])` for all `j` such that the fruit at `j` can cover the remaining fruits up to `i`. Specifically, if we buy fruit `i`, we cover up to `2*i` fruits.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of fruits, as each element is added and removed from the deque at most once.
- **Space Complexity**: `O(n)` to store the DP array and the deque.

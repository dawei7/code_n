# Maximum Coins From K Consecutive Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3413 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Official Link | [maximum-coins-from-k-consecutive-bags](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) |

## Problem Description & Examples
### Goal
Given a set of non-overlapping intervals representing bags of coins, determine the maximum number of coins you can collect by choosing a contiguous range of length `k`. The range can partially overlap with the bags, in which case you collect a proportional amount of coins from that bag.

### Function Contract
**Inputs**

- `coins`: A list of lists where each element `[start, end, coins]` represents a bag covering the range `[start, end]` containing `coins` total.
- `k`: An integer representing the length of the window you can place on the number line.

**Return value**

- An integer representing the maximum possible coins collected.

### Examples
**Example 1**

- Input: `coins = [[8,10,1],[1,3,2],[5,6,4]], k = 2`
- Output: `6`

**Example 2**

- Input: `coins = [[1,10,3]], k = 2`
- Output: `1`

**Example 3**

- Input: `coins = [[1,10,3]], k = 12`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Sorting**, **Prefix Sums**, and the **Sliding Window** technique. First, we sort the bags by their start positions. We then compute prefix sums of the coins to allow $O(1)$ range queries. For each bag, we consider two scenarios: the window ends at the bag's end or starts at the bag's start. We use binary search (`bisect_right`) to efficiently find the range of bags fully contained within the window of length `k` and handle the partial overlaps at the boundaries.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the number of bags. Sorting takes $O(n \log n)$, and iterating through the bags with binary search takes $O(n \log n)$.
- **Space Complexity**: $O(n)$ to store the prefix sums and the sorted list of bags.

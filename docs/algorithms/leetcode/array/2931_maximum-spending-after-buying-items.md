# Maximum Spending After Buying Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2931 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [maximum-spending-after-buying-items](https://leetcode.com/problems/maximum-spending-after-buying-items/) |

## Problem Description & Examples
### Goal
You are given a 2D grid of prices where each row represents a shop's inventory, sorted in non-decreasing order. You must purchase every single item across all shops over a series of days. On day `d` (starting from 1), you buy one item. The cost of an item is multiplied by `d`. To maximize your total spending, you must strategically choose which item to buy each day, always picking from the available items at the end of each shop's row.

### Function Contract
**Inputs**

- `values`: A list of lists of integers (`List[List[int]]`), where `values[i][j]` represents the price of the `j`-th item in the `i`-th shop.

**Return value**

- An integer representing the maximum total cost accumulated after purchasing all items.

### Examples
**Example 1**

- Input: `values = [[8,5,2],[6,4,1],[9,7,3]]`
- Output: `285`

**Example 2**

- Input: `values = [[10,8,6,4,2],[9,7,5,3,1]]`
- Output: `386`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach** combined with a **Min-Heap (Priority Queue)**. Since we want to maximize the total sum and the multiplier `d` increases daily, we should prioritize buying the smallest available items first (to save the larger values for higher multipliers). Because each row is sorted, the smallest available item in any shop is always at the current end of the row. We maintain a min-heap of the last elements of all rows to efficiently extract the global minimum across all shops.

---

## Complexity Analysis
- **Time Complexity**: `O(N * M * log(N))`, where `N` is the number of shops and `M` is the number of items per shop. We perform `N * M` extractions from the heap, and each heap operation takes `O(log N)`.
- **Space Complexity**: `O(N)`, as the heap stores at most one element from each of the `N` shops.

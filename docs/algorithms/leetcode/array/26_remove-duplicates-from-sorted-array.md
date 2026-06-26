# Remove Duplicates from Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_28` |
| Frontend ID | 26 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [remove-duplicates-from-sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |

## Problem Description & Examples
### Goal
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. Find the maximum profit you can achieve by buying on one day and selling on a later day. If no profit is possible, return 0.

### Function Contract
**Inputs**

- `prices`: List[int]

**Return value**

int - maximum profit

### Examples
**Example 1**

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`

**Example 2**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

**Example 3**

- Input: `prices = [1, 2]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

# Trapping Rain Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_35` |
| Frontend ID | 42 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack |
| Official Link | [trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/) |

## Problem Description & Examples
### Goal
Given an integer array `fruits` where `fruits[i]` is the type of fruit on tree `i`, you can pick from at most 2 types of fruits (two baskets). Find the maximum number of fruits you can pick in a contiguous subarray.

### Function Contract
**Inputs**

- `fruits`: List[int]

**Return value**

int - max fruits pickable with 2 baskets

### Examples
**Example 1**

- Input: `fruits = [1, 2, 1]`
- Output: `3`

**Example 2**

- Input: `fruits = [3]`
- Output: `1`

**Example 3**

- Input: `fruits = [1, 0]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

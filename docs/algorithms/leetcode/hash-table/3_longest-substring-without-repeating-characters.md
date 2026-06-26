# Longest Substring Without Repeating Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_38` |
| Frontend ID | 3 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |

## Problem Description & Examples
### Goal
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

`solve(operations)` processes `['push', val]`, `['pop']`, `['top']`, `['get_min']` operations and returns results from `top` and `get_min`.

### Function Contract
**Inputs**

- `operations`: List[List] - push/pop/top/get_min operations

**Return value**

List[int] - results of top and get_min operations

### Examples
**Example 1**

- Input: `[["push", -2], ["push", 0], ["get_min"]]`
- Output: `[-2]`

**Example 2**

- Input: `operations = [['push', 94], ['get_min'], ['push', -34], ['pop']]`
- Output: `[94]`

**Example 3**

- Input: `operations = [['push', 45], ['push', -35], ['push', 26], ['get_min']]`
- Output: `[-35]`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

# Sliding Window Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_44` |
| Frontend ID | 239 |
| Difficulty | Hard |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Official Link | [sliding-window-maximum](https://leetcode.com/problems/sliding-window-maximum/) |

## Problem Description & Examples
### Goal
Given an array of integers `heights` representing the histogram bar heights (width=1), find the area of the largest rectangle in the histogram.

### Function Contract
**Inputs**

- `heights`: List[int]

**Return value**

int - area of largest rectangle

### Examples
**Example 1**

- Input: `heights = [2, 1, 5, 6, 2, 3]`
- Output: `10`

**Example 2**

- Input: `heights = [12, 13]`
- Output: `24`

**Example 3**

- Input: `heights = [4, 18]`
- Output: `18`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

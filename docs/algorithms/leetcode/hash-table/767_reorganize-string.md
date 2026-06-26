# Reorganize String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_118` |
| Frontend ID | 767 |
| Difficulty | Medium |
| Topics | Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting |
| Official Link | [reorganize-string](https://leetcode.com/problems/reorganize-string/) |

## Problem Description & Examples
### Goal
Given a string `s`, rearrange the characters so no two adjacent characters are the same. Return any such arrangement, or `""` if impossible.

### Function Contract
**Inputs**

- `s`: str

**Return value**

str - rearranged string or empty if impossible

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `"aba"`

**Example 2**

- Input: `s = 'aa'`
- Output: `''`

**Example 3**

- Input: `s = 'aaa'`
- Output: `''`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

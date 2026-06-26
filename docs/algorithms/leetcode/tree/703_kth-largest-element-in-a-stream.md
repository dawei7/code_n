# Kth Largest Element in a Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_111` |
| Frontend ID | 703 |
| Difficulty | Easy |
| Topics | Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream |
| Official Link | [kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) |

## Problem Description & Examples
### Goal
Design a class that finds the k-th largest element in a stream. `solve(k, nums, stream)` returns the k-th largest after each number added from `stream`.

### Function Contract
**Inputs**

- `k`: int
- `nums`: List[int] - initial numbers
- `stream`: List[int] - added numbers

**Return value**

List[int] - k-th largest after each add

### Examples
**Example 1**

- Input: `k = 3, nums = [4, 5, 8, 2], stream = [3, 5, 10, 9, 4]`
- Output: `[4, 5, 5, 8, 8]`

**Example 2**

- Input: `k = 2, nums = [98, 54], stream = [6, 34]`
- Output: `[54, 54]`

**Example 3**

- Input: `k = 1, nums = [73], stream = [98, 9]`
- Output: `[98, 98]`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

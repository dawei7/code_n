# Find Median from Data Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_121` |
| Frontend ID | 295 |
| Difficulty | Hard |
| Topics | Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream |
| Official Link | [find-median-from-data-stream](https://leetcode.com/problems/find-median-from-data-stream/) |

## Problem Description & Examples
### Goal
Design a data structure that supports adding numbers from a stream and finding the median efficiently. `solve(stream)` returns the median after each number added.

### Function Contract
**Inputs**

- `stream`: List[int]

**Return value**

List[float] - running median after each number

### Examples
**Example 1**

- Input: `stream = [1, 2, 3, 4, 5]`
- Output: `[1.0, 1.5, 2.0, 2.5, 3.0]`

**Example 2**

- Input: `stream = [50, 98]`
- Output: `[50.0, 74.0]`

**Example 3**

- Input: `stream = [18, 73]`
- Output: `[18.0, 45.5]`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

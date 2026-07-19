# Find Median from Data Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 295 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) |

## Problem Description
### Goal
Design a `MedianFinder` that receives integers one at a time through `addNum`. All inserted occurrences remain part of the data set, including duplicates and negative values, and later insertions must not invalidate earlier state.

`findMedian()` returns the middle value after sorting when the count is odd, or the arithmetic mean of the two middle values when the count is even. Report the result as a floating-point value. Support repeated queries and insertions efficiently without sorting the complete history after every call. The app adapter inserts a supplied stream and returns the median after each prefix; the native class exposes the operations separately.

### Function Contract
**Inputs**

- `stream`: the integers in arrival order

**Return value**

A floating-point list whose element at index `i` is the median of `stream[:i+1]`.

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

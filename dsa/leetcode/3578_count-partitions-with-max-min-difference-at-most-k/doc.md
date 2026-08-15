# Count Partitions With Max-Min Difference at Most K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3578 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Sliding Window, Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/) |

## Problem Description

### Goal

Partition an integer array `nums` into one or more non-empty contiguous segments. Every array element must belong to exactly one segment and the segments must retain their original order.

A segment is valid when the difference between its maximum and minimum elements is at most `k`. Count all ways to choose the segment boundaries so that every resulting segment is valid. Because the count may be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2\le n\le5\cdot10^4$ and $1\le\texttt{nums[i]}\le10^9$.
- `k`: The maximum permitted difference within each segment, where $0\le k\le10^9$.

**Return value**

Return the number of valid contiguous partitions modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [9,4,1,3,7], k = 4`
- **Output:** `6`
- **Explanation:** Six choices of segment boundaries keep every segment's maximum-minus-minimum difference at most `4`.

#### Example 2

- **Input:** `nums = [3,3,4], k = 0`
- **Output:** `2`
- **Explanation:** The two equal `3` values may be grouped together or separated, while `4` must form its own segment.

---

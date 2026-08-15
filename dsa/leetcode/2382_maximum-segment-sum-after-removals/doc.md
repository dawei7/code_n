# Maximum Segment Sum After Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2382 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Prefix Sum, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-segment-sum-after-removals/) |

## Problem Description

### Goal

You are given two 0-indexed integer arrays, `nums` and `removeQueries`, of the same length. Initially every entry of `nums` is present. Process the queries in order; query `i` removes the element at index `removeQueries[i]`. Every removal may shorten a current segment, split it into two segments, or eliminate it.

A segment is a contiguous sequence of positive entries that have not been removed, and its segment sum is the sum of those entries. After every removal, find the greatest sum among all remaining segments. Return one answer for each query. If no entries remain, the maximum segment sum is zero. Every array index appears exactly once in `removeQueries`, so no position is removed twice.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `removeQueries`: A permutation of the indices from $0$ through $n-1$ that gives the removal order.

**Return value**

- Return a list of length $n$ whose entry at index `i` is the maximum remaining segment sum after applying removal `i`.

**Segment semantics**

- Removed positions separate segments; values on opposite sides of a removed position are not contiguous.
- Segment sums may exceed 32-bit signed integer range.
- After the final query there are no segments, so the final answer is `0`.

### Examples

#### Example 1

- **Input:** `nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]`
- **Output:** `[14,7,2,2,0]`
- **Explanation:** After removing index `0`, the remaining segment sums to 14. Removing index `3` splits it, leaving `[2,5]` as the largest segment with sum 7.

#### Example 2

- **Input:** `nums = [3,2,11,1], removeQueries = [3,2,1,0]`
- **Output:** `[16,5,3,0]`
- **Explanation:** The surviving prefix has sums 16, 5, and 3 after the first three removals; the last removal leaves no segment.

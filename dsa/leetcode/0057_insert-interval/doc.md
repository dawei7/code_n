# Insert Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 57 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-interval/) |

## Problem Description
### Goal
You are given closed intervals sorted in ascending order by start, with every pair non-overlapping, plus one new closed interval. Insert the new interval at its proper position. Because endpoints are included, touching or intersecting intervals must merge.

Return a new sorted, non-overlapping interval list that covers exactly the original intervals together with the insertion. The new interval may belong before all existing intervals, after them, or may connect several consecutive intervals into one. The supplied interval values should not be modified as a side effect.

### Function Contract
**Inputs**

- `intervals`: a sorted `List[List[int]]` of pairwise-disjoint closed intervals
- `new_interval`: the `[start, end]` interval to insert

**Return value**

The new sorted list after insertion and merging.

### Examples
**Example 1**

- Input: `intervals = [[1,3],[6,9]], new_interval = [2,5]`
- Output: `[[1,5],[6,9]]`

**Example 2**

- Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]`
- Output: `[[1,2],[3,10],[12,16]]`

**Example 3**

- Input: `intervals = [], new_interval = [5,7]`
- Output: `[[5,7]]`

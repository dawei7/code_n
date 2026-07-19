# Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 435 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) |

## Problem Description
### Goal
Given intervals `[start, end]` with `start < end`, remove selected intervals so that every pair left in the collection is nonoverlapping. Intervals that only meet at a shared endpoint are compatible and may both remain.

Return the minimum number of removals needed. Input order has no scheduling significance, and several optimal retained sets may exist. Removing one interval can resolve conflicts with several others, so counting overlapping pairs is not the answer. The function returns only the number removed, not the retained intervals or their reordered schedule. A one-interval input requires zero removals.

### Function Contract
**Inputs**

- `intervals`: a list of `[start, end]` pairs with `start < end`

**Return value**

- Return the minimum number of intervals that must be removed; intervals that only touch at an endpoint do not overlap.

### Examples
**Example 1**

- Input: `intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]`
- Output: `1`

**Example 2**

- Input: `intervals = [[1, 2], [1, 2], [1, 2]]`
- Output: `2`

**Example 3**

- Input: `intervals = [[1, 2], [2, 3]]`
- Output: `0`

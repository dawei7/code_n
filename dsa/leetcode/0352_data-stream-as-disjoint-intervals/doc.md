# Data Stream as Disjoint Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 352 |
| Difficulty | Hard |
| Topics | Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) |

## Problem Description
### Goal
Design a `SummaryRanges` structure that receives nonnegative integers one at a time through `addNum(value)`. It must represent every distinct value seen so far using closed integer intervals, combining consecutive values into the same interval.

`getIntervals()` returns the smallest collection of disjoint intervals covering the current values, sorted by starting point in ascending order. A new value may create an isolated interval, extend one interval, or bridge and merge two neighbors. Repeated insertions change nothing. Preserve state across operations, and return snapshots whose interval boundaries reflect all additions made before that query without including unseen gap values.

### Function Contract
**Inputs**

- `values`: for the app adapter, stream values added in order. Native LeetCode calls `addNum(value)` and `getIntervals()` separately.

**Return value**

- The app adapter returns the interval snapshot after every insertion. Each snapshot is sorted by start. Native `getIntervals()` returns the current snapshot.

### Examples
**Example 1**

- Input: `values = [1, 3, 7, 2, 6]`
- Output: `[[[1,1]], [[1,1],[3,3]], [[1,1],[3,3],[7,7]], [[1,3],[7,7]], [[1,3],[6,7]]]`

**Example 2**

- Input: `values = [1, 2, 3]`
- Output: `[[[1,1]], [[1,2]], [[1,3]]]`

**Example 3**

- Input: `values = [5, 5]`
- Output: `[[[5,5]], [[5,5]]]`

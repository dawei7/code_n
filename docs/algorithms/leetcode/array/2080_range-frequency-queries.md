# Range Frequency Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2080 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Design, Segment Tree |
| Official Link | [range-frequency-queries](https://leetcode.com/problems/range-frequency-queries/) |

## Problem Description & Examples
### Goal
Design a structure that answers how often a value appears within an inclusive index range.

### Function Contract
**Inputs**

- Initial `arr`: integer array.
- Query arguments: `left`, `right`, and `value`.

**Return value**

Each query returns the frequency of `value` in `arr[left:right+1]`.

### Examples
**Example 1**

- Input: `["RangeFreqQuery","query","query"], [[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]`
- Output: `[null,1,2]`

**Example 2**

- Input: `arr = [1,1,2,2,2], query(0,4,2), query(0,1,2)`
- Output: `[3,0]`

**Example 3**

- Input: `arr = [5], query(0,0,5), query(0,0,1)`
- Output: `[1,0]`

---

## Underlying Base Algorithm(s)
Precompute a sorted list of positions for each value. A query binary-searches that position list for the first index `>= left` and first index `> right`; their difference is the frequency.

---

## Complexity Analysis
- **Time Complexity**: `O(log f)` per query, where `f` is occurrences of the value.
- **Space Complexity**: `O(n)`

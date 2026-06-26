# Summary Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 228 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [summary-ranges](https://leetcode.com/problems/summary-ranges/) |

## Problem Description & Examples
### Goal
Summarize a sorted array of distinct integers as maximal consecutive ranges.

### Function Contract
**Inputs**

- `nums`: strictly increasing integers.

**Return value**

A string per maximal range: a single number as `"a"`, or a multi-number range as `"a->b"`.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 4, 5, 7]`
- Output: `["0->2", "4->5", "7"]`

**Example 2**

- Input: `nums = [0, 2, 3, 4, 6, 8, 9]`
- Output: `["0", "2->4", "6", "8->9"]`

**Example 3**

- Input: `nums = []`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Track the start and previous value of the current run. Extend while each value equals `previous + 1`; otherwise emit the finished run and begin a new one. Emit the final run after the scan.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding output strings

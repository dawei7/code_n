# Check if All the Integers in a Range Are Covered

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1893 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [check-if-all-the-integers-in-a-range-are-covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) |

## Problem Description & Examples
### Goal
Given several inclusive integer ranges, check whether every integer from `left` through `right` is covered by at least one range.

### Function Contract
**Inputs**

- `ranges`: a list of `[start, end]` inclusive ranges.
- `left`: start of the target interval.
- `right`: end of the target interval.

**Return value**

Return `True` if the whole target interval is covered, otherwise `False`.

### Examples
**Example 1**

- Input: `ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5`
- Output: `True`

**Example 2**

- Input: `ranges = [[1,10],[10,20]], left = 21, right = 21`
- Output: `False`

**Example 3**

- Input: `ranges = [[1,5]], left = 1, right = 5`
- Output: `True`

---

## Underlying Base Algorithm(s)
For the small fixed value range, mark covered integers in a boolean array and verify every target value. A difference-array variant can mark whole intervals and prefix-sum coverage counts.

---

## Complexity Analysis
- **Time Complexity**: `O(number of covered values + right - left)`
- **Space Complexity**: `O(1)` because the value range is bounded

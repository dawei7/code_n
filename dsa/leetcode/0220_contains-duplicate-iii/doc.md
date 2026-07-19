# Contains Duplicate III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 220 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Sliding Window, Sorting, Bucket Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/contains-duplicate-iii/) |

## Problem Description
### Goal
Given an integer array and nonnegative bounds `indexDiff` and `valueDiff`, find whether two distinct positions are close in both index and value. A pair `(i, j)` qualifies when `abs(i - j) <= indexDiff` and `abs(nums[i] - nums[j]) <= valueDiff`.

Return `True` if any pair satisfies both inequalities; otherwise return `False`. The values need not be equal unless `valueDiff` is zero, and nearby values at positions outside the index window do not qualify. One occurrence cannot pair with itself, so arrays with fewer than two elements and all cases with `indexDiff = 0` return `False`.

### Function Contract
**Inputs**

- `nums`: an integer list
- `indexDiff`: maximum index distance
- `valueDiff`: maximum absolute value distance

**Return value**

`True` when one pair satisfies both bounds; otherwise `False`.

### Examples
**Example 1**

- Input: `[1,2,3,1], 3, 0`
- Output: `True`

**Example 2**

- Input: `[1,5,9,1,5,9], 2, 3`
- Output: `False`

**Example 3**

- Input: `[1,4], 1, 3`
- Output: `True`

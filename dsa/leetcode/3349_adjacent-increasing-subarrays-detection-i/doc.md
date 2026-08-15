# Adjacent Increasing Subarrays Detection I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3349 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, determine whether the array contains two contiguous subarrays of exactly `k` elements each such that every subarray is strictly increasing. A subarray is strictly increasing when each element after the first is greater than the element immediately before it within that subarray.

The two chosen subarrays must be adjacent and non-overlapping. If the first starts at index `a`, the second must start at index `a + k`; the comparison across their shared boundary is irrelevant because the boundary elements belong to different subarrays. Return whether at least one valid adjacent pair exists.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers.
- `k`: The exact length required for each of the two subarrays.

The source guarantees $2 \le n \le 100$, $1 < 2k \le n$, and $-1000 \le \texttt{nums[i]} \le 1000$.

**Return value**

- Return `True` when two adjacent strictly increasing subarrays of length `k` exist; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k = 3`
- **Output:** `True`
- **Explanation:** `[7, 8, 9]` and `[2, 3, 4]` are strictly increasing length-three subarrays whose starting indices differ by three.

#### Example 2

- **Input:** `nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k = 5`
- **Output:** `False`
- **Explanation:** No two adjacent blocks of five elements are both strictly increasing.

**Boundary example**

- **Input:** `nums = [1, 2, 2, 3], k = 2`
- **Output:** `True`
- **Explanation:** `[1, 2]` and `[2, 3]` are each strictly increasing; equality between the last value of the first block and the first value of the second does not invalidate either block.

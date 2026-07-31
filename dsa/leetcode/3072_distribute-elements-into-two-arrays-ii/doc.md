# Distribute Elements Into Two Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3072 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Segment Tree, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/) |

## Problem Description

### Goal

Given a 1-indexed integer array `nums` of length $n$, distribute its values between two arrays, `arr1` and `arr2`. For an array `arr` and a value `val`, define `greaterCount(arr, val)` as the number of elements in `arr` that are strictly greater than `val`.

The first operation appends `nums[1]` to `arr1`, and the second appends `nums[2]` to `arr2`. For every later index $i$, compare `greaterCount(arr1, nums[i])` with `greaterCount(arr2, nums[i])`. Append `nums[i]` to the array whose count is larger.

When the two greater counts are equal, append the value to the array that currently contains fewer elements. If both arrays also have equal lengths, append it to `arr1`.

Return the result formed by concatenating `arr1` followed by `arr2`. The order in which values were appended within each array must be preserved.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- The list `arr1 + arr2` after all $n$ distribution operations.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3, 3]`
- Output: `[2, 3, 1, 3]`
- Explanation: Both greater counts are zero for each `3`. The first `3` goes to `arr1` because the lengths are tied; the second goes to the now-shorter `arr2`.

**Example 2**

- Input: `nums = [5, 14, 3, 1, 2]`
- Output: `[5, 3, 1, 2, 14]`
- Explanation: The first count tie sends `3` to `arr1`. For both `1` and `2`, `arr1` then contains more strictly greater values than `arr2`.

**Example 3**

- Input: `nums = [3, 3, 3, 3]`
- Output: `[3, 3, 3, 3]`
- Explanation: Equal values are never strictly greater, so length and final `arr1` tie-breaking alternate the placements evenly.

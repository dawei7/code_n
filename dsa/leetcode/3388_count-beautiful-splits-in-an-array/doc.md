# Count Beautiful Splits in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3388 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-beautiful-splits-in-an-array/) |

## Problem Description

### Goal

Split `nums` into three non-empty contiguous subarrays `nums1`, `nums2`, and `nums3` whose concatenation, in that order, is the original array.

A split is beautiful when at least one of two prefix relations holds: `nums1` is a prefix of `nums2`, or `nums2` is a prefix of `nums3`. Being a prefix requires every element of the shorter candidate to equal the corresponding starting element of the other subarray; it also requires the candidate prefix to be no longer than that subarray.

Return the number of distinct choices for the two cut positions that produce a beautiful split. A split satisfying both prefix relations is counted only once.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers.

The bounds are $1 \le n \le 5000$ and $0 \le \texttt{nums[i]} \le 50$.

**Return value**

Return the number of beautiful ways to divide `nums` into three non-empty contiguous subarrays.

### Examples

#### Example 1

- **Input:** `nums = [1, 1, 2, 1]`
- **Output:** `2`
- **Explanation:** The valid divisions are `[1] | [1, 2] | [1]` and `[1] | [1] | [2, 1]`.

#### Example 2

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `0`

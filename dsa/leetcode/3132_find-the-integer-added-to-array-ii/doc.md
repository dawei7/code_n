# Find the Integer Added to Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3132 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-integer-added-to-array-ii/) |

## Problem Description

### Goal

You are given two integer arrays, `nums1` and `nums2`. Exactly two elements must be removed from `nums1`. After those removals, every remaining element is increased by the same integer $x$; when $x$ is negative, this operation decreases each value instead.

The transformed `nums1` must be equal to `nums2`, where equality means that both arrays contain the same integers with the same frequencies, regardless of order. The input guarantees that at least one valid choice of two removals and an integer $x$ exists. Return the minimum possible value of $x$ among all valid choices.

### Function Contract

**Inputs**

- `nums1`: A list of integers with length between $3$ and $200$, inclusive.
- `nums2`: A list whose length is exactly `len(nums1) - 2`.

Every element of both arrays is between $0$ and $1000$, inclusive.

**Return value**

- Return the minimum integer $x$ for which removing exactly two elements from `nums1` and adding $x$ to every remaining element produces the same multiset as `nums2`.

### Examples

#### Example 1

- **Input:** `nums1 = [4, 20, 16, 12, 8], nums2 = [14, 18, 10]`
- **Output:** `-2`
- **Explanation:** Remove the values at indices `0` and `4`. Adding `-2` to `[20, 16, 12]` produces `[18, 14, 10]`.

#### Example 2

- **Input:** `nums1 = [3, 5, 5, 3], nums2 = [7, 7]`
- **Output:** `2`
- **Explanation:** Remove the two values equal to `3`, then add `2` to the remaining pair.

# Split Array With Same Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 805 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-with-same-average/) |

## Problem Description

### Goal

Given an integer array `nums`, move every element into exactly one of two arrays `A` and `B`. Both groups must be nonempty, but they do not need to be contiguous and their internal order does not matter.

Return `True` if the partition can make $\operatorname{avg}(A) = \operatorname{avg}(B)$, and `False` otherwise. Each occurrence is assigned once even when values repeat, and an average is the group's sum divided by its number of elements.

### Function Contract

**Inputs**

- `nums`: a nonempty list of nonnegative integers.

**Return value**

- `True` if some nonempty proper subset has the same average as its complement; otherwise, `False`.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5,6,7,8]`
- Output: `True`
- Explanation: `[1,8]` and the remaining six values both have average `4.5`.

**Example 2**

- Input: `nums = [3,1]`
- Output: `False`
- Explanation: The only split produces singleton averages `3` and `1`.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `True`
- Explanation: The subset `[2]` and its complement `[1,3]` both average `2`.

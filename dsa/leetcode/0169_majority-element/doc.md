# Majority Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 169 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/majority-element/) |

## Problem Description
### Goal
Given a nonempty list of integers, one value is guaranteed to appear more than $\left\lfloor n / 2 \right\rfloor$ times. Other values may repeat as well, and occurrences of the majority need not be adjacent or appear in any particular order.

Return the majority value itself. Its frequency must be strictly greater than half the list length, not merely tied for the highest frequency. Negative values and zero are valid candidates. Meet the intended linear-time and constant-extra-space target rather than sorting the array or building a frequency table proportional to the number of distinct values.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list containing a guaranteed majority element

**Return value**

The majority value.

### Examples
**Example 1**

- Input: `nums = [3,2,3]`
- Output: `3`

**Example 2**

- Input: `nums = [2,2,1,1,1,2,2]`
- Output: `2`

**Example 3**

- Input: `nums = [7]`
- Output: `7`

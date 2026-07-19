# Summary Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 228 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/summary-ranges/) |

## Problem Description
### Goal
Given a unique integer array `nums` sorted in ascending order, divide its values into maximal ranges of consecutive integers. A range continues while each next value is exactly one greater than the previous value and ends at any larger gap.

Return one string per run in the original ascending order. Represent a one-value run as `"a"`, and a run containing at least two values from `a` through `b` as `"a->b"`. Every input value must belong to exactly one summary range, ranges may not bridge missing integers, and an empty input produces an empty list.

### Function Contract
**Inputs**

- `nums`: a strictly increasing list of distinct integers

**Return value**

A list of strings. A one-value range is written as `"a"`; a longer range from `a` through `b` is written as `"a->b"`.

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

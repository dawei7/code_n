# Two Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum/) |

## Problem Description
### Goal
You are given an integer array `nums` and an integer `target`. Choose two different positions whose stored values add exactly to the target, then return those positions rather than the values themselves. Array values may repeat, so equal numbers at distinct indices remain separate choices.

Every input is guaranteed to contain exactly one valid pair. An index cannot be selected twice, even when doubling one value would equal the target. Return the two indices in any order; no result for any other pair is required.

### Function Contract
**Inputs**

- `nums`: the integer array
- `target`: the required pair sum

**Return value**

A two-element list containing distinct indices whose values sum to `target`.

### Examples
**Example 1**

- Input: `nums = [2, 7, 11, 15], target = 9`
- Output: `[0, 1]`

**Example 2**

- Input: `nums = [3, 2, 4], target = 6`
- Output: `[1, 2]`

**Example 3**

- Input: `nums = [3, 3], target = 6`
- Output: `[0, 1]`

# Largest Number At Least Twice of Others

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 747 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) |

## Problem Description

### Goal

Given an integer array `nums` whose largest value is unique, determine whether that largest element is at least twice as large as every other number in the array.

If it satisfies the condition for all other positions, return the zero-based index of the largest element. Otherwise return `-1`. Equality with exactly twice another value qualifies, while failing the comparison against even one other number makes the answer `-1`.

### Function Contract

**Inputs**

- `nums`: a list of non-negative integers with a unique maximum value.

**Return value**

- The maximum value's original index when it is at least twice every other value; otherwise `-1`.

### Examples

**Example 1**

- Input: `nums = [3, 6, 1, 0]`
- Output: `1`
- Explanation: `6` is at least twice each of `3`, `1`, and `0`.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `-1`
- Explanation: The maximum `4` is not at least twice `3`.

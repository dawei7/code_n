# Bitwise AND of Numbers Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

## Problem Description
### Goal
Given two nonnegative integers `left` and `right` with `left <= right`, consider every integer in the inclusive interval between them. Combine all of those values using the bitwise AND operation, retaining a bit only when it is set in every member of the range.

Return the resulting integer. Both endpoints participate, so an interval containing one value returns that value unchanged, while bits that flip anywhere inside a larger interval become zero. The range may be too large to enumerate value by value, so meet the required logarithmic or fixed-bit-width behavior rather than iterating across every integer.

### Function Contract
**Inputs**

- `left`: the nonnegative lower endpoint
- `right`: the nonnegative upper endpoint, at least `left`

**Return value**

The bitwise AND of all integers in the range.

### Examples
**Example 1**

- Input: `left = 5, right = 7`
- Output: `4`

**Example 2**

- Input: `left = 0, right = 0`
- Output: `0`

**Example 3**

- Input: `left = 49, right = 62`
- Output: `48`

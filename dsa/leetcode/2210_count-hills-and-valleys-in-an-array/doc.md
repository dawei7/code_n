# Count Hills and Valleys in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2210 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, classify an interior value as part of a hill when its closest non-equal neighbors on both sides are smaller, or as part of a valley when both such neighbors are larger.

Adjacent equal values belong to one shared hill or valley rather than separate features. An index without a non-equal neighbor on either side cannot qualify. Return the total number of distinct hills and valleys represented by the array.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $3 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

Return the number of distinct hill and valley features, counting each plateau of equal adjacent values at most once.

### Examples

**Example 1**

- Input: `nums = [2, 4, 1, 1, 6, 5]`
- Output: `3`
- Explanation: `4` is a hill, the adjacent `1` values form one valley, and `6` is a hill.

**Example 2**

- Input: `nums = [6, 6, 5, 5, 4, 1]`
- Output: `0`
- Explanation: after equal plateaus are treated as single values, the sequence decreases throughout.

**Example 3**

- Input: `nums = [1, 2, 2, 1]`
- Output: `1`
- Explanation: the two adjacent `2` values form one hill.

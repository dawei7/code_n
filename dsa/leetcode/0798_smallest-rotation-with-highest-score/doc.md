# Smallest Rotation with Highest Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 798 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-rotation-with-highest-score/) |

## Problem Description

### Goal

Given an array `nums` of length `n`, rotate it left by `k` positions so that the suffix beginning at `k` moves before the original prefix. In the rotated array, an element at index `i` earns one point when its value is less than or equal to `i`.

Choose `k` from `0` through $n - 1$ to maximize the total score. Return the smallest rotation amount among all choices attaining that highest score; each element contributes at most one point.

### Function Contract

**Inputs**

- `nums`: a nonempty list of length `n` whose values lie between `0` and $n - 1$.

**Return value**

- The smallest rotation amount in $[0, n - 1]$ attaining the highest score.

### Examples

**Example 1**

- Input: `nums = [2,3,1,4,0]`
- Output: `3`
- Explanation: Rotating left three places produces `[4,0,2,3,1]`, where four values are no greater than their indices; no earlier rotation scores as highly.

**Example 2**

- Input: `nums = [1,3,0,2,4]`
- Output: `0`
- Explanation: The original arrangement already achieves the maximum score, so the smallest maximizing rotation is zero.

**Example 3**

- Input: `nums = [0,0,0]`
- Output: `0`
- Explanation: Every rotation scores all three positions, and the smallest tied rotation is zero.

# Smallest Index With Equal Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2057 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-index-with-equal-value/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums`, examine each index `i` and compare the remainder of `i` divided by $10$ with the value stored at that position. An index qualifies exactly when `i % 10 == nums[i]`.

Return the smallest qualifying index. If no array position satisfies the equality, return `-1`. Because values range from $0$ through $9$, the modulo comparison repeats its possible index-side values every ten positions.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$ and $0 \le \texttt{nums[i]} \le 9$.

**Return value**

- Return the smallest index `i` satisfying `i % 10 == nums[i]`, or `-1` when none exists.

### Examples

**Example 1**

- Input: `nums = [0,1,2]`
- Output: `0`
- Explanation: Every index qualifies, so the smallest is zero.

**Example 2**

- Input: `nums = [4,3,2,1]`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3,4,5,6,7,8,9,0]`
- Output: `-1`

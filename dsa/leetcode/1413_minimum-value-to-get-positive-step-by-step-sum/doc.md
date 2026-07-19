# Minimum Value to Get Positive Step by Step Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1413 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) |

## Problem Description

### Goal

Begin with a positive integer `startValue`, then process `nums` from left to right. At each step, add the current array value to the running total that started at `startValue`. Every intermediate total, including the total after each array element, must be at least $1$.

Return the minimum positive `startValue` that satisfies this condition for the entire array. The choice must cover the deepest cumulative drop, even when that lowest point occurs after an earlier recovery.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$ and $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

- The smallest positive integer starting value for which every step-by-step sum is at least $1$.

### Examples

**Example 1**

- Input: `nums = [-3,2,-3,4,2]`
- Output: `5`

**Example 2**

- Input: `nums = [1,2]`
- Output: `1`

**Example 3**

- Input: `nums = [1,-2,-3]`
- Output: `5`

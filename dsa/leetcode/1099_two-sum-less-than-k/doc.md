# Two Sum Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1099 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/two-sum-less-than-k/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, choose indices $i < j$ and let their values form the sum `nums[i] + nums[j]`. Among every such pair whose sum is strictly less than `k`, return the maximum sum.

The two values must come from different indices, although their numeric values may be equal. If no pair has a sum strictly below `k`, return `-1`.

### Function Contract

**Inputs**

- `nums`: an array of $n$ integers, where $1 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 1000$.
- `k`: the strict upper bound for the pair sum, where $1 \leq \texttt{k} \leq 2000$.

**Return value**

The greatest value of `nums[i] + nums[j]` over distinct indices $i < j$ for which the sum is less than `k`, or `-1` when no valid pair exists.

### Examples

**Example 1**

- Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60`
- Output: `58`

Values 34 and 24 produce 58, and no valid pair has a larger sum below 60.

**Example 2**

- Input: `nums = [10, 20, 30], k = 15`
- Output: `-1`

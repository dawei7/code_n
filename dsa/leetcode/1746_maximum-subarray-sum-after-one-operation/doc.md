# Maximum Subarray Sum After One Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1746 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/) |

## Problem Description

### Goal

You are given an integer array `nums`. Perform exactly one operation: choose one array element and replace it by its square. After that replacement, select a nonempty contiguous subarray.

Return the largest subarray sum that can be achieved by choosing both the squared position and the subarray optimally. The squared element may originally be positive, negative, or zero, and the selected subarray may start and end anywhere.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array with $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum sum of a nonempty contiguous subarray after exactly one element of `nums` has been replaced by its square.

### Examples

**Example 1**

- Input: `nums = [2,-1,-4,-3]`
- Output: `17`
- Explanation: Squaring `-4` gives the subarray `[2,-1,16]`, whose sum is $17$.

**Example 2**

- Input: `nums = [1,-1,1,1,-1,-1,1]`
- Output: `4`
- Explanation: Squaring a selected `-1` changes it to `1`, allowing a best sum of $4$.

**Example 3**

- Input: `nums = [-5]`
- Output: `25`
- Explanation: The only element must be squared and is also the only nonempty subarray.

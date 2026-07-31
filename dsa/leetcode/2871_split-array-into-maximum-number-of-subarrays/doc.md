# Split Array Into Maximum Number of Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2871 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Split Array Into Maximum Number of Subarrays](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/) |

## Problem Description

### Goal

You are given an array `nums` of non-negative integers. The score of a nonempty subarray `nums[l..r]` is the bitwise AND of every value from index `l` through index `r`.

Split the array into one or more contiguous, nonempty subarrays so that every element belongs to exactly one part. Among all such splits, first minimize the sum of the subarray scores. Subject to that minimum total score, return the maximum possible number of subarrays.

### Function Contract

**Inputs**

- `nums`: A nonempty list of non-negative integers.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- The maximum number of contiguous subarrays among all splits whose sum of bitwise-AND scores is minimum.

### Examples

**Example 1**

- Input: `nums = [1,0,2,0,1,2]`
- Output: `3`
- Explanation: The subarrays `[1,0]`, `[2,0]`, and `[1,2]` each have score zero, so their total score is the minimum possible value, zero.

**Example 2**

- Input: `nums = [5,7,1,3]`
- Output: `1`
- Explanation: The bitwise AND of the whole array is `1`. Keeping all elements together attains that minimum score, while every split into multiple subarrays has a larger score sum.

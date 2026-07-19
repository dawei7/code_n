# Maximum Absolute Sum of Any Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1749 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) |

## Problem Description

### Goal

You are given an integer array `nums`. For a contiguous subarray, its absolute sum is the absolute value of the ordinary sum of all elements in that subarray: a negative total is negated, while a nonnegative total is unchanged.

Return the maximum absolute sum among all possibly empty contiguous subarrays. The empty subarray has sum zero, so the answer is always nonnegative. A winning subarray may therefore have either a large positive total or a strongly negative total whose magnitude is larger; both directions must be considered.

### Function Contract

**Inputs**

- `nums`: a nonempty list of integers with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

- Return the largest value of $\left\lvert\sum_{k=l}^{r}\texttt{nums[k]}\right\rvert$ over all contiguous index ranges, also allowing the empty range with sum zero.

### Examples

**Example 1**

- Input: `nums = [1, -3, 2, 3, -4]`
- Output: `5`
- Explanation: The subarray `[2, 3]` has sum `5`, whose absolute value is `5`.

**Example 2**

- Input: `nums = [2, -5, 1, -4, 3, -2]`
- Output: `8`
- Explanation: The subarray `[-5, 1, -4]` sums to `-8`, giving absolute sum `8`.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `0`
- Explanation: Every subarray, including the empty one, has sum zero.

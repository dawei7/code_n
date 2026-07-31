# Count Subarrays With Fixed Bounds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2444 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) |

## Problem Description

### Goal

You are given an integer array `nums` and two integers `minK` and `maxK`. A fixed-bound subarray is a contiguous portion of `nums` whose minimum element is exactly `minK` and whose maximum element is exactly `maxK`.

Count all fixed-bound subarrays and return the total. Subarrays with different start or end indices count separately, even when their sequences of values happen to be equal.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $2 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.
- `min_k`: The required minimum value, with $1 \le \texttt{min\_k} \le 10^6$.
- `max_k`: The required maximum value, with $1 \le \texttt{max\_k} \le 10^6$.

**Return value**

- The number of contiguous subarrays whose minimum is `min_k` and whose maximum is `max_k`.

### Examples

**Example 1**

- Input: `nums = [1, 3, 5, 2, 7, 5], min_k = 1, max_k = 5`
- Output: `2`
- Explanation: The valid subarrays are `[1, 3, 5]` and `[1, 3, 5, 2]`.

**Example 2**

- Input: `nums = [1, 1, 1, 1], min_k = 1, max_k = 1`
- Output: `10`
- Explanation: Every nonempty subarray has both required bounds.

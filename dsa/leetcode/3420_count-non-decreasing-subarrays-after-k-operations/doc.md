# Count Non-Decreasing Subarrays After K Operations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/) |
| Frontend ID | 3420 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For each contiguous subarray of `nums`, you may perform at most `k` operations. One operation increments any chosen element of that subarray by exactly `1`. Decide independently for every subarray whether some allowed sequence of increments can make its elements non-decreasing.

Changes considered for one subarray do not modify `nums` for any other subarray. Count and return all subarrays that can be made non-decreasing within their own operation budget. A sequence is non-decreasing when every element after the first is at least its predecessor.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The maximum number of increments available separately to each subarray, where $1 \le k \le 10^9$.

**Return value**

Return the number of contiguous subarrays whose elements can be made non-decreasing using at most `k` increments.

### Examples

**Example 1**

- Input: `nums = [6,3,1,2,4,4]`, `k = 7`
- Output: `17`
- Explanation: Among the 21 subarrays, exactly the four starting with `[6,3,1]` and extending through positions 2, 3, 4, or 5 require more than seven increments.

**Example 2**

- Input: `nums = [6,3,1,3,6]`, `k = 4`
- Output: `12`
- Explanation: `[3,1,3,6]` is the only valid length-four subarray, and every subarray of length at most three is valid except `[6,3,1]`.

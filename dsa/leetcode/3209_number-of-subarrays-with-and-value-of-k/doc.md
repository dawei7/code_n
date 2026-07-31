# Number of Subarrays With AND Value of K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3209 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/) |

## Problem Description

### Goal

Given `nums` and a target integer `k`, consider every nonempty contiguous subarray. Compute the bitwise AND of all values in that subarray.

For a chosen interval, a bit remains set in its result only when that bit is set in every element of the interval. The interval must use consecutive positions; elements cannot be skipped or reordered.

Return the total number of subarrays whose AND is exactly `k`. Subarrays are distinguished by their start and end indices, even when their values are identical.

### Function Contract

**Inputs**

- `nums`: A nonempty integer array with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $0 \le \texttt{nums}[i] \le 10^9$.
- `k`: The required bitwise-AND value, with $0 \le k \le 10^9$.

Let $n=\lvert\texttt{nums}\rvert$ and $M=1+\max(\texttt{nums})$.

**Return value**

- The number of nonempty contiguous subarrays whose element-wise bitwise AND equals `k`.

### Examples

**Example 1**

- Input: `nums = [1,1,1], k = 1`
- Output: `6`
- Explanation: All six nonempty subarrays contain only ones and therefore have AND value `1`.

**Example 2**

- Input: `nums = [1,1,2], k = 1`
- Output: `3`
- Explanation: The two singleton `1` subarrays and the length-two prefix have AND value `1`.

**Example 3**

- Input: `nums = [1,2,3], k = 2`
- Output: `2`
- Explanation: The singleton `[2]` and subarray `[2,3]` have AND value `2`.

# Maximum Good Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3026 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-good-subarray-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. A nonempty contiguous subarray `nums[i..j]` is **good** when the absolute difference between its first and last values is exactly `k`:

$$
\lvert \texttt{nums[i]}-\texttt{nums[j]} \rvert=k.
$$

Return the maximum sum among all good subarrays. Values inside the chosen interval do not affect whether it is good, but they do contribute to its sum. The maximum may be negative; return `0` only when no pair of endpoints in the array satisfies the required difference.

### Function Contract

**Inputs**

- `nums`: A list of $N$ integers, where $2\le N\le10^5$ and $-10^9\le\texttt{nums[i]}\le10^9$.
- `k`: A positive integer with $1\le k\le10^9$.

**Return value**

The maximum sum of a good contiguous subarray, or `0` if no good subarray exists.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5, 6], k = 1`
- **Output:** `11`

The good adjacent intervals end with consecutive values; `[5, 6]` has the largest sum, `11`.

#### Example 2

- **Input:** `nums = [-1, 3, 2, 4, 5], k = 3`
- **Output:** `11`

The good interval `[2, 4, 5]` begins with `2`, ends with `5`, and has sum `11`.

#### Example 3

- **Input:** `nums = [-1, -2, -3, -4], k = 2`
- **Output:** `-6`

The good intervals are `[-1, -2, -3]` and `[-2, -3, -4]`; the larger of their negative sums is `-6`.

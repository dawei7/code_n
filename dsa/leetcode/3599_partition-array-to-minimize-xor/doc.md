# Partition Array to Minimize XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3599 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-to-minimize-xor/) |

## Problem Description
### Goal
Divide an integer array `nums` into exactly `k` nonempty contiguous subarrays. Compute the bitwise XOR of all elements inside each subarray, producing one score for every part. A partition's cost is the largest of those `k` scores.

Choose the `k - 1` cut positions so that this largest score is as small as possible, and return that minimum cost. The order of the elements cannot change, every element must belong to one part, and no part may be empty.

### Function Contract
**Inputs**

- `nums`: the positive integer array to partition
- `k`: the exact number of nonempty contiguous subarrays required

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 250$, $1 \le \texttt{nums[i]} \le 10^9$, and $1 \le k \le n$.

**Return value**

The minimum possible value of the maximum subarray XOR among all valid partitions into exactly `k` parts.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `1`

The partition `[1]` and `[2, 3]` has XOR scores `1` and `1`, so its maximum is `1`.

**Example 2**

- Input: `nums = [2, 3, 3, 2], k = 3`
- Output: `2`

Using `[2]`, `[3, 3]`, and `[2]` produces scores `2`, `0`, and `2`.

**Example 3**

- Input: `nums = [1, 1, 2, 3, 1], k = 2`
- Output: `0`

The two parts `[1, 1]` and `[2, 3, 1]` both have XOR `0`.

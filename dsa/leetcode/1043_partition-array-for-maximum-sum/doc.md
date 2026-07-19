# Partition Array for Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1043 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/partition-array-for-maximum-sum/) |

## Problem Description

### Goal

Given an integer array `arr`, partition it into contiguous subarrays, each having length at most `k`.

After choosing the partition, replace every value in each subarray by the maximum value originally contained in that same subarray. Return the largest possible sum of the transformed array over all valid partitions. The test cases guarantee that the answer fits in a 32-bit integer.

### Function Contract

**Inputs**

- `arr`: an array of length $N$, where $1 \le N \le 500$ and $0 \le \texttt{arr[i]} \le 10^9$.
- `k`: the maximum partition length $K$, where $1 \le K \le N$.

**Return value**

- The maximum transformed-array sum obtainable by partitioning `arr` into contiguous subarrays of length at most $K$.

### Examples

**Example 1**

- Input: `arr = [1,15,7,9,2,5,10], k = 3`
- Output: `84`
- Explanation: One optimal partition transforms the array into `[15,15,15,9,10,10,10]`.

**Example 2**

- Input: `arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4`
- Output: `83`

**Example 3**

- Input: `arr = [1], k = 1`
- Output: `1`

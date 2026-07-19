# K Inverse Pairs Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 629 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/k-inverse-pairs-array/) |

## Problem Description
### Goal
For an integer array `nums`, an inverse pair is a pair of indices `[i, j]` with `0 <= i < j < len(nums)` and `nums[i] > nums[j]`. Given integers `n` and `k`, consider all different arrays that use each number from `1` through `n` exactly once.

Return how many of these permutations contain exactly `k` inverse pairs. Because the count can be very large, return it modulo `1,000,000,007`. When `k` is outside the possible range from `0` through $n(n - 1) / 2$, the answer is `0`.

### Function Contract
**Inputs**

- `n`: the permutation length
- `k`: the required number of pairs `(i, j)` with $i < j$ and `permutation[i] > permutation[j]`

**Return value**

- The number of qualifying permutations modulo `1,000,000,007`
- Return zero when `k` exceeds the maximum $n(n - 1) / 2$

### Examples
**Example 1**

- Input: `n = 3`, `k = 0`
- Output: `1`

**Example 2**

- Input: `n = 3`, `k = 1`
- Output: `2`

**Example 3**

- Input: `n = 4`, `k = 2`
- Output: `5`

# K-Concatenation Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1191 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [k-concatenation-maximum-sum](https://leetcode.com/problems/k-concatenation-maximum-sum/) |

## Problem Description & Examples
### Goal
Concatenate `arr` with itself `k` times and find the maximum sum of a non-empty subarray, returning the value modulo `1_000_000_007`. A negative best sum is reported as `0`.

### Function Contract
**Inputs**

- `arr`: integer array.
- `k`: number of concatenations.

**Return value**

The maximum subarray sum in the concatenated array, modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `arr = [1,2]`, `k = 3`
- Output: `9`

**Example 2**

- Input: `arr = [1,-2,1]`, `k = 5`
- Output: `2`

**Example 3**

- Input: `arr = [-1,-2]`, `k = 7`
- Output: `0`

---

## Underlying Base Algorithm(s)
Kadane's algorithm with prefix/suffix reasoning.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

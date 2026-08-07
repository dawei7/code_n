## Description

Given an integer array `nums` and an integer `k`, return *the maximum length of a **subarray** that sums to* `k`. If there is not one, return `0` instead.
### Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are considered.
- `k`: The required subarray sum.

**Return value**

Return the maximum number of elements in a contiguous subarray summing to `k`, or `0` when there is none.

### Examples
#### Example 1

- **Input:** `nums = [1,-1,5,-2,3], k = 3`
- **Output:** `4`
- **Explanation:** The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#### Example 2

- **Input:** `nums = [-2,-1,2,1], k = 1`
- **Output:** `2`
- **Explanation:** The subarray [-1, 2] sums to 1 and is the longest.
### Constraints

- $1 \le \text{nums.length} \le 2 * 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- $-10^{9} \le k \le 10^{9}$
## Description

Given an integer array `nums`, return `true`* if there exists a triple of indices *`(i, j, k)`* such that *`i < j < k`* and *$\text{nums}[i] < \text{nums}[j] < \text{nums}[k]$. If no such indices exists, return `false`.
### Function Contract

**Inputs**

- `nums`: The integer array in which index order must be preserved.

**Return value**

Return `true` when `nums` contains a strictly increasing subsequence of length three; otherwise return `false`.

### Examples
#### Example 1

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `true`
- **Explanation:** Any triplet where i < j < k is valid.
#### Example 2

- **Input:** `nums = [5,4,3,2,1]`
- **Output:** `false`
- **Explanation:** No triplet exists.
#### Example 3

- **Input:** `nums = [2,1,5,0,4,6]`
- **Output:** `true`
- **Explanation:** One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
### Constraints

- $1 \le \text{nums.length} \le 5 * 10^{5}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

**Follow up:** Could you implement a solution that runs in `O(n)` time complexity and `O(1)` space complexity?
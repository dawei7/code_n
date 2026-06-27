# Sum of Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2615 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [sum-of-distances](https://leetcode.com/problems/sum-of-distances/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate for each element at index `i` the sum of absolute differences between `i` and all other indices `j` where the values at `i` and `j` are identical.

### Function Contract
**Inputs**

- `nums`: A list of integers where `1 <= nums.length <= 10^5`.

**Return value**

- A list of integers `arr` where `arr[i]` is the sum of distances for `nums[i]`.

### Examples
**Example 1**

- Input: `nums = [1, 3, 1, 1, 2]`
- Output: `[5, 0, 3, 4, 0]`

**Example 2**

- Input: `nums = [0, 5, 3]`
- Output: `[0, 0, 0]`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `[2, 1, 2]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Map to group indices by their corresponding values. For each group of indices, we use the Prefix Sum technique to calculate the sum of absolute differences in linear time. Specifically, for a sorted list of indices `idx_list`, the sum of distances for an index `idx_list[i]` is calculated as:
`(i * idx_list[i] - prefix_sum[i]) + ((total_sum - prefix_sum[i+1]) - (count - 1 - i) * idx_list[i])`.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the input array. We iterate through the array once to group indices and once more to compute the sums.
- **Space Complexity**: `O(N)` to store the hash map of indices and the resulting array.

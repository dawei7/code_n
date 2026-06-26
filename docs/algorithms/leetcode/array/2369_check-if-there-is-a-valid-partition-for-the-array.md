# Check if There is a Valid Partition For The Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2369 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [check-if-there-is-a-valid-partition-for-the-array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/) |

## Problem Description & Examples
### Goal
Determine if an integer array can be partitioned into one or more contiguous subarrays, where each subarray must satisfy one of three specific conditions: it contains two equal elements, three equal elements, or three consecutive increasing elements (with a difference of 1).

### Function Contract
**Inputs**

- `nums`: A list of integers where 0 <= nums[i] <= 10^6.

**Return value**

- A boolean indicating whether a valid partition of the entire array exists.

### Examples
**Example 1**

- Input: `nums = [4,4,4,5,6]`
- Output: `true`
- Explanation: The array can be partitioned into [4,4] and [4,5,6].

**Example 2**

- Input: `nums = [1,1,1,2]`
- Output: `false`
- Explanation: No valid partition exists for the given array.

**Example 3**

- Input: `nums = [3,3,3]`
- Output: `true`
- Explanation: The array can be partitioned into [3,3,3].

---

## Underlying Base Algorithm(s)
Dynamic Programming (Bottom-Up). We maintain a boolean array `dp` where `dp[i]` represents whether the prefix of the array of length `i` can be validly partitioned. The state transition checks if the last 2 or 3 elements satisfy the required conditions and if the preceding prefix was also valid.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once.
- **Space Complexity**: O(n) to store the DP table (can be optimized to O(1) by only keeping track of the last three states).

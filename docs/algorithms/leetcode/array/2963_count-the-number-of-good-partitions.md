# Count the Number of Good Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2963 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Combinatorics |
| Official Link | [count-the-number-of-good-partitions](https://leetcode.com/problems/count-the-number-of-good-partitions/) |

## Problem Description & Examples
### Goal
Given an array of integers, a partition is considered "good" if every element present in one subarray does not appear in any other subarray. We need to determine the total number of ways to partition the array into one or more such good subarrays. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 10^5 and 1 <= nums[i] <= 10^9.

**Return value**

- An integer representing the number of valid partitions modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 2, 1, 3]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem relies on identifying "boundaries" where a partition can occur. An element's range is defined by its first and last occurrence. If two ranges overlap, they must belong to the same partition. By calculating the last occurrence of every element, we can iterate through the array and maintain a `max_reach` pointer. Whenever our current index matches `max_reach`, we have completed a valid, independent block. If there are `k` such independent blocks, there are `k-1` possible cut points, leading to `2^(k-1)` total ways to partition the array.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array. We traverse the array twice: once to map the last indices and once to identify the partition boundaries.
- **Space Complexity**: `O(N)` to store the hash map of the last occurrence indices.

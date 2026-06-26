# Count Subarrays With Median K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2488 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [count-subarrays-with-median-k](https://leetcode.com/problems/count-subarrays-with-median-k/) |

## Problem Description & Examples
### Goal
Given an array of distinct integers and a target value `k`, determine the total number of contiguous subarrays where the median is exactly `k`. For an array of length `n`, the median is defined as the element at index `(n-1)/2` in the sorted version of the subarray.

### Function Contract
**Inputs**

- `nums`: A list of distinct integers.
- `k`: An integer that must be present in the array.

**Return value**

- An integer representing the count of subarrays whose median is `k`.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 4, 5], k = 4`
- Output: `3`
- Explanation: The subarrays are `[4]`, `[4, 5]`, and `[1, 4, 5]`.

**Example 2**

- Input: `nums = [2, 3, 1], k = 3`
- Output: `1`
- Explanation: The only subarray is `[3]`.

**Example 3**

- Input: `nums = [1], k = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Prefix Sum** approach combined with a **Hash Map**. We transform the array into a sequence of `+1` (if `nums[i] > k`), `-1` (if `nums[i] < k`), and `0` (if `nums[i] == k`). A subarray has median `k` if the sum of these transformed values is either `0` (for odd length) or `1` (for even length). We track the prefix sums to the left of `k` in a hash map and compare them with prefix sums to the right of `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array once to find `k` and once to compute prefix sums.
- **Space Complexity**: `O(n)` to store the frequency of prefix sums in the hash map.

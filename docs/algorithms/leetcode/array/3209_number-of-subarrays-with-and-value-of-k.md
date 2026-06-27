# Number of Subarrays With AND Value of K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3209 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Official Link | [number-of-subarrays-with-and-value-of-k](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/) |

## Problem Description & Examples
### Goal
Given an array of integers and a target integer `k`, determine the total count of contiguous subarrays where the bitwise AND of all elements within the subarray equals `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers (1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^9).
- `k`: An integer (0 <= k <= 10^9).

**Return value**

- An integer representing the total count of subarrays whose bitwise AND result is exactly `k`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`

**Example 2**

- Input: `nums = [1, 1, 2], k = 1`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
The solution leverages the property that for a fixed right endpoint of a subarray, the bitwise AND value is non-increasing as the left endpoint moves to the left. Furthermore, there are at most O(log(max(nums))) distinct bitwise AND values ending at any index `i`. We maintain a dictionary (or list of pairs) representing the counts of all possible AND values ending at the current index. By iterating through the array once and updating these values, we can efficiently count the occurrences of `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`, where `n` is the length of the array. Since each element has at most 30 bits, the number of distinct AND values is bounded by the number of bits.
- **Space Complexity**: `O(log(max(nums)))` to store the active AND values and their frequencies for the current index.

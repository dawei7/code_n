# Number of Subarrays With GCD Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2447 |
| Difficulty | Medium |
| Topics | Array, Math, Number Theory |
| Official Link | [number-of-subarrays-with-gcd-equal-to-k](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/) |

## Problem Description & Examples
### Goal
Given an integer array and a target integer `k`, determine the total count of contiguous subarrays where the greatest common divisor (GCD) of all elements within that subarray is exactly equal to `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums[i] <= 10^6.
- `k`: An integer representing the target GCD value.

**Return value**

- An integer representing the total number of contiguous subarrays whose GCD equals `k`.

### Examples
**Example 1**

- Input: `nums = [9, 3, 1, 2, 6, 3], k = 3`
- Output: `4`
- Explanation: The subarrays are [9, 3], [3], [3], [6, 3].

**Example 2**

- Input: `nums = [4], k = 7`
- Output: `0`
- Explanation: No subarray has a GCD of 7.

**Example 3**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`
- Explanation: All possible subarrays have a GCD of 1.

---

## Underlying Base Algorithm(s)
The solution utilizes the property that the GCD of a subarray is non-increasing as the subarray expands. By iterating through each starting index and expanding the subarray, we can maintain a running GCD. Since the GCD of a sequence can only change at most O(log(max(nums))) times, we can efficiently count valid subarrays.

---

## Complexity Analysis
- **Time Complexity**: O(n * log(max(nums))), where n is the length of the array. For each starting position, the GCD value changes at most logarithmic times relative to the maximum value in the array.
- **Space Complexity**: O(1), as we only use a few variables to track the current GCD and the running count.

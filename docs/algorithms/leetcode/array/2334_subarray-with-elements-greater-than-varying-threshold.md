# Subarray With Elements Greater Than Varying Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2334 |
| Difficulty | Hard |
| Topics | Array, Stack, Union-Find, Monotonic Stack |
| Official Link | [subarray-with-elements-greater-than-varying-threshold](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `threshold`, determine if there exists any contiguous subarray such that every element within that subarray is strictly greater than `threshold` divided by the subarray's length. If such a subarray is found, return its length. If multiple such subarrays exist, any valid length is acceptable. If no such subarray satisfies the condition, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array. `0 <= nums.length <= 10^5`. `1 <= nums[i] <= 10^9`.
- `threshold`: An integer. `0 <= threshold <= 10^9`.

**Return value**

- An integer representing the length of a valid subarray, or -1 if no such subarray exists.

### Examples
**Example 1**

- Input: `nums = [1,3,4,3,1]`, `threshold = 6`
- Output: `3`
- Explanation:
  - Consider the subarray `[3,4,3]` (indices 1 to 3), which has a length of 3.
  - The minimum element in this subarray is 3.
  - The condition is `min_element > threshold / length`.
  - `3 > 6 / 3` simplifies to `3 > 2`, which is true.
  - Thus, 3 is a valid length. (Another valid length is 2 for `[3,4]` where `min=3`, `3 > 6/2` is `3 > 3` which is false. Wait, `[3,4]` min is 3, length 2. `3 > 6/2` is `3 > 3` which is false. My manual check was wrong. Let's re-evaluate.
  - `[3,4]` (length 2): min is 3. `3 > 6/2` (3 > 3) is false.
  - `[4]` (length 1): min is 4. `4 > 6/1` (4 > 6) is false.
  - `[1,3,4,3,1]` (length 5): min is 1. `1 > 6/5` (1 > 1.2) is false.
  - The output 3 for `[3,4,3]` is correct.

**Example 2**

- Input: `nums = [6,5,6,5,6]`, `threshold = 10`
- Output: `5`
- Explanation:
  - Consider the subarray `[6,5,6,5,6]` (indices 0 to 4), which has a length of 5.
  - The minimum element in this subarray is 5.
  - The condition is `min_element > threshold / length`.
  - `5 > 10 / 5` simplifies to `5 > 2`, which is true.
  - Thus, 5 is a valid length. (Another valid length is 3 for `[6,5,6]` where `min=5`, `5 > 10/3` is `5 > 3.33...` which is true.)

**Example 3**

- Input: `nums = [1,2,3]`, `threshold = 10`
- Output: `-1`
- Explanation:
  - For any possible subarray, the condition `min_element > threshold / length` will not be met.
  - E.g., for `[1,2,3]` (length 3), min is 1. `1 > 10/3` (1 > 3.33...) is false.
  - E.g., for `[3]` (length 1), min is 3. `3 > 10/1` (3 > 10) is false.

---

## Underlying Base Algorithm(s)
The core idea is to rephrase the condition `min_val_in_subarray > threshold / length_of_subarray` as `min_val_in_subarray * length_of_subarray > threshold`. This transformation avoids floating-point arithmetic and potential precision issues.

For each element `nums[i]` in the array, we can consider it as the minimum element of a potential subarray. If `nums[i]` is the minimum element in a subarray `nums[l...r]`, then all elements `nums[j]` where `l <= j <= r` must satisfy `nums[j] >= nums[i]`. To maximize the length of such a subarray for a given `nums[i]` (and thus maximize `nums[i] * length`), we need to find the largest possible range `[l, r]` such that `nums[i]` is the minimum within `nums[l...r]`.

This is a classic problem that can be solved efficiently using a **Monotonic Stack**.
1.  **Find `left_smaller` array:** For each index `i`, find the index `j` of the first element to its left (`j < i`) such that `nums[j] < nums[i]`. If no such element exists, `j` is considered -1. A monotonic increasing stack can compute this in O(N) time.
2.  **Find `right_smaller` array:** For each index `i`, find the index `j` of the first element to its right (`j > i`) such that `nums[j] < nums[i]`. If no such element exists, `j` is considered `n` (where `n` is the length of `nums`). A monotonic increasing stack (iterating from right to left) can compute this in O(N) time.

Once `left_smaller[i]` and `right_smaller[i]` are known for all `i`, the largest subarray for which `nums[i]` is the minimum element spans from `left_smaller[i] + 1` to `right_smaller[i] - 1`. The length of this subarray is `L = (right_smaller[i] - 1) - (left_smaller[i] + 1) + 1 = right_smaller[i] - left_smaller[i] - 1`.

Finally, iterate through each `i` from `0` to `n-1`. Calculate `L` using the precomputed `left_smaller` and `right_smaller` values. If `nums[i] * L > threshold`, then we have found a valid subarray of length `L`, and we can return `L`. If the loop completes without finding such a subarray, return -1.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`
  - Computing `left_smaller` array using a monotonic stack takes O(N) time.
  - Computing `right_smaller` array using a monotonic stack takes O(N) time.
  - Iterating through `nums` once to check the condition takes O(N) time.
  - Overall, the time complexity is dominated by these linear passes, resulting in O(N).
- **Space Complexity**: `O(N)`
  - `left_smaller` array requires O(N) space.
  - `right_smaller` array requires O(N) space.
  - The monotonic stack itself requires O(N) space in the worst case (e.g., a strictly increasing or decreasing array).
  - Overall, the space complexity is O(N).

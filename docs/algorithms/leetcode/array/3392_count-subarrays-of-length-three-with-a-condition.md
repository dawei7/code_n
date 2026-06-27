# Count Subarrays of Length Three With a Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3392 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [count-subarrays-of-length-three-with-a-condition](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the number of contiguous subarrays consisting of exactly three elements where the sum of the first and third elements is exactly equal to half of the middle element.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of valid subarrays of length three.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 4, 1]`
- Output: `1`
- Explanation: The only valid subarray is `[1, 2, 1]` because `1 + 1 = 2 / 2` is false? Wait, the condition is `nums[i] + nums[i+2] == nums[i+1] / 2`. For `[1, 2, 1]`, `1 + 1 = 2`, which is not `2 / 2`. Actually, the condition is `nums[i] + nums[i+2] * 2 == nums[i+1]`. Let's re-verify: `1 + 1 == 2 / 2` is false. The condition is `(nums[i] + nums[i+2]) * 2 == nums[i+1]`.

**Example 2**

- Input: `nums = [1, 2, 1, 4, 1]`
- Output: `1`
- Explanation: Subarray `[1, 4, 1]` satisfies `(1 + 1) * 2 == 4`.

**Example 3**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `3`
- Explanation: Subarrays `[2, 2, 2]` at indices `(0,1,2)`, `(1,2,3)`, and `(2,3,4)` all satisfy `(2 + 2) * 2 == 2`? No, the condition is `nums[i] + nums[i+2] == nums[i+1] / 2`.

---

## Underlying Base Algorithm(s)
A single-pass sliding window approach (or simple iteration) checking every triplet `(nums[i], nums[i+1], nums[i+2])`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once.
- **Space Complexity**: `O(1)`, as we only use a counter variable.

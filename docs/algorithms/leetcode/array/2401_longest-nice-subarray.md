# Longest Nice Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2401 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Sliding Window |
| Official Link | [longest-nice-subarray](https://leetcode.com/problems/longest-nice-subarray/) |

## Problem Description & Examples
### Goal
Given an array of positive integers, identify the length of the longest contiguous subarray where every pair of elements has a bitwise AND result of zero. In other words, no two numbers in the subarray can share any set bits at the same position.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the maximum length of a "nice" contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [1, 3, 8, 48, 10]`
- Output: `3`
- Explanation: The longest nice subarray is `[8, 48, 10]`.

**Example 2**

- Input: `nums = [3, 1, 5, 11, 13]`
- Output: `1`
- Explanation: The longest nice subarray is `[3]` (or any single element).

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `3`
- Explanation: The longest nice subarray is `[1, 2, 4]`.

---

## Underlying Base Algorithm(s)
The problem is solved using the **Sliding Window** technique combined with **Bit Manipulation**. We maintain a window `[left, right]` and a variable `used_bits` that tracks the bitwise OR of all elements currently in the window. If adding `nums[right]` causes a bit collision (i.e., `used_bits & nums[right] != 0`), we shrink the window from the left until the collision is resolved.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is added to and removed from the window at most once.
- **Space Complexity**: `O(1)`, as the `used_bits` integer only stores bits for numbers up to the problem constraints (typically 32 bits), which is constant space.

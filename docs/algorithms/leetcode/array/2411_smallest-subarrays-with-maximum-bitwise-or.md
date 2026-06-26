# Smallest Subarrays With Maximum Bitwise OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2411 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Bit Manipulation, Sliding Window |
| Official Link | [smallest-subarrays-with-maximum-bitwise-or](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) |

## Problem Description & Examples
### Goal
Given an array of integers, for every index `i`, determine the length of the shortest subarray starting at `i` that achieves the maximum possible bitwise OR value among all subarrays starting at `i`.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- A list of integers where the element at index `i` represents the length of the shortest subarray starting at `i` that yields the maximum possible bitwise OR value for that starting position.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2, 1, 3]`
- Output: `[3, 3, 2, 2, 1]`

**Example 2**

- Input: `nums = [1, 2]`
- Output: `[2, 1]`

**Example 3**

- Input: `nums = [0, 0]`
- Output: `[1, 1]`

---

## Underlying Base Algorithm(s)
The problem can be solved by tracking the most recent index at which each bit (0-29) was set to 1. Since the bitwise OR operation is monotonic (adding more elements can only increase or maintain the OR value), the maximum OR for a subarray starting at `i` is achieved by including all bits that appear at or after index `i`. To minimize the subarray length, we find the furthest index among the "last seen" positions of all bits present in the global maximum OR.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the length of the array and `k` is the number of bits (30). Since `k` is constant, this is effectively `O(n)`.
- **Space Complexity**: `O(k)`, as we only need to store the last seen index for each of the 30 bits.

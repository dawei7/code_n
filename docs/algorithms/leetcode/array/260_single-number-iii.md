# Single Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 260 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [single-number-iii](https://leetcode.com/problems/single-number-iii/) |

## Problem Description & Examples
### Goal
Given an integer array where every element appears exactly twice except for two elements that appear only once, identify and return those two unique elements. The order of the returned elements does not matter.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where every number appears twice except for two distinct numbers.

**Return value**

- A list of two integers (`List[int]`) representing the two unique numbers found in the input array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 3, 2, 5]`
- Output: `[3, 5]`

**Example 2**

- Input: `nums = [-1, 0]`
- Output: `[-1, 0]`

**Example 3**

- Input: `nums = [0, 1]`
- Output: `[1, 0]`

---

## Underlying Base Algorithm(s)
The solution utilizes the properties of the XOR bitwise operator. XORing a number with itself results in 0, and XORing a number with 0 results in the number itself. By XORing all elements in the array, the result is the XOR sum of the two unique numbers (let's call them `a` and `b`). Since `a != b`, the result `a ^ b` must have at least one bit set to 1. We isolate the rightmost set bit of `a ^ b` to create a mask. We then partition the original array into two groups based on whether each number has that specific bit set or not. XORing each group independently will cancel out the pairs, leaving only `a` in one group and `b` in the other.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform two linear passes over the input.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space regardless of the input size.

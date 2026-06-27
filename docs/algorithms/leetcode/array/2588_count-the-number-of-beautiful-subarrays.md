# Count the Number of Beautiful Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2588 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Bit Manipulation, Prefix Sum |
| Official Link | [count-the-number-of-beautiful-subarrays](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, a subarray is considered "beautiful" if you can reduce all its elements to zero by repeatedly choosing two indices and performing a bitwise AND operation on the elements at those indices, effectively allowing you to flip bits. More simply, a subarray is beautiful if the XOR sum of all its elements is zero, as the operation allows any two elements to be reduced if their bits can be cleared through the AND operation, which is equivalent to the condition that the total XOR sum of the subarray is zero.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the total count of contiguous subarrays whose elements can be reduced to zero.

### Examples
**Example 1**

- Input: `nums = [4,3,1,2,4]`
- Output: `2`

**Example 2**

- Input: `nums = [1,10,4]`
- Output: `0`

**Example 3**

- Input: `nums = [0,0,0]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem relies on the property of the XOR operation. A subarray `nums[i...j]` has an XOR sum of zero if the prefix XOR sum up to `j` is equal to the prefix XOR sum up to `i-1`. By maintaining a hash map (frequency table) of prefix XOR sums encountered so far, we can count how many times a specific prefix XOR value has appeared. For every current prefix XOR value, the number of previously seen identical prefix XOR values represents the number of beautiful subarrays ending at the current index.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once and perform constant-time hash map lookups.
- **Space Complexity**: `O(n)` in the worst case, as we may store up to `n` distinct prefix XOR values in the hash map.

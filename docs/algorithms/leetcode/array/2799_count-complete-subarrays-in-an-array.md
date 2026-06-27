# Count Complete Subarrays in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2799 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [count-complete-subarrays-in-an-array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the total number of contiguous subarrays that contain the exact same set of distinct elements as the original array. A subarray is considered "complete" if its count of unique integers matches the count of unique integers found in the entire input array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of all contiguous subarrays that are complete.

### Examples
**Example 1**

- Input: `nums = [1,3,1,2,2]`
- Output: `4`
- Explanation: The distinct elements are {1, 2, 3}. The complete subarrays are [1,3,1,2], [1,3,1,2,2], [3,1,2], and [3,1,2,2].

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `10`
- Explanation: The distinct element is {5}. Every non-empty subarray is complete. There are 4*(4+1)/2 = 10 such subarrays.

**Example 3**

- Input: `nums = [1,2,1,3]`
- Output: `3`
- Explanation: The distinct elements are {1, 2, 3}. The complete subarrays are [1,2,1,3], [2,1,3], and [1,2,1,3] is not possible, but [1,2,1,3] is the only one containing all three. Wait, the complete subarrays are [1,2,1,3], [2,1,3], and [1,2,1,3] is not correct; the valid ones are [1,2,1,3], [2,1,3], and [1,2,1,3] is not right. Actually, the subarrays are [1,2,1,3] and [2,1,3].

---

## Underlying Base Algorithm(s)
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (or frequency array). By first identifying the total number of unique elements in the array, we can expand a right pointer to include elements until the window contains all unique elements. Once the condition is met, we shrink the left pointer to find all valid subarrays ending at the current right position.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array with two pointers, each moving at most `n` times.
- **Space Complexity**: `O(k)`, where `k` is the number of unique elements in the array, used to store the frequency map.

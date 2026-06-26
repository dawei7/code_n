# Count the Number of Good Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2537 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [count-the-number-of-good-subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, determine the total number of contiguous subarrays that qualify as "good." A subarray is defined as "good" if it contains at least `k` pairs of identical elements. A pair is defined as two indices `(i, j)` such that `i < j` and `nums[i] == nums[j]`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the minimum number of identical pairs required.

**Return value**

- An integer representing the total count of good subarrays.

### Examples
**Example 1**

- Input: `nums = [1,1,1,1,1], k = 10`
- Output: `1`
- Explanation: The only subarray with at least 10 pairs is the entire array itself.

**Example 2**

- Input: `nums = [3,1,4,3,2,2,4], k = 2`
- Output: `4`
- Explanation: The good subarrays are [3,1,4,3,2,2], [3,1,4,3,2,2,4], [1,4,3,2,2,4], and [4,3,2,2,4].

**Example 3**

- Input: `nums = [1,2,3], k = 1`
- Output: `0`
- Explanation: No subarray contains any identical pairs.

---

## Underlying Base Algorithm(s)
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (frequency dictionary). We maintain a window `[left, right]` and track the current number of pairs. When adding an element `x` that has appeared `n` times previously, we increment the pair count by `n`. When removing an element `x` that appears `n` times in the current window, we decrement the pair count by `n-1`. Since the number of pairs is monotonic with respect to the window size, we can efficiently count valid subarrays.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is added and removed from the window at most once.
- **Space Complexity**: `O(n)` in the worst case to store the frequency map of elements within the current window.

# Count of Interesting Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2845 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [count-of-interesting-subarrays](https://leetcode.com/problems/count-of-interesting-subarrays/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the total number of contiguous subarrays where the count of elements satisfying a specific condition (being congruent to `k` modulo `m`) results in a value that is also congruent to `k` modulo `m`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `modulo`: An integer `m`.
- `k`: An integer `k`.

**Return value**

- An integer representing the total count of "interesting" subarrays.

### Examples
**Example 1**

- Input: `nums = [3, 2, 4], modulo = 2, k = 1`
- Output: `3`
- Explanation: The interesting subarrays are [3], [3, 2], and [3, 2, 4].

**Example 2**

- Input: `nums = [3, 1, 9, 6], modulo = 3, k = 0`
- Output: `2`
- Explanation: The interesting subarrays are [3] and [9].

**Example 3**

- Input: `nums = [11, 12, 21, 14], modulo = 10, k = 1`
- Output: `1`
- Explanation: The interesting subarray is [11].

---

## Underlying Base Algorithm(s)
The problem is solved using the **Prefix Sum** technique combined with a **Hash Map (Frequency Table)**. By transforming the array into a binary sequence where an element is `1` if `nums[i] % modulo == k` and `0` otherwise, the problem reduces to finding subarrays whose sum `S` satisfies `S % modulo == k`. We maintain a running prefix sum and store the frequency of each `(prefix_sum % modulo)` encountered so far to calculate the number of valid subarrays ending at the current index in constant time.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(min(n, modulo))`, as the hash map stores at most `modulo` distinct remainders.

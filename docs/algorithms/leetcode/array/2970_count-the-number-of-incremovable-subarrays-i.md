# Count the Number of Incremovable Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2970 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Binary Search, Enumeration |
| Official Link | [count-the-number-of-incremovable-subarrays-i](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the total number of subarrays that, when removed, leave the remaining elements in a strictly increasing order. A subarray is defined as a contiguous sequence of elements within the array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of all possible subarrays whose removal results in a strictly increasing sequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`
- Explanation: All subarrays are incremovable because removing any contiguous part leaves the remaining elements sorted.

**Example 2**

- Input: `nums = [6, 5, 7, 8]`
- Output: `7`
- Explanation: The subarrays that can be removed are [6], [5], [6, 5], [5, 7], [6, 5, 7], [5, 7, 8], and [6, 5, 7, 8].

**Example 3**

- Input: `nums = [8, 7, 6, 6]`
- Output: `3`
- Explanation: The valid subarrays to remove are [8, 7, 6], [7, 6, 6], and [8, 7, 6, 6].

---

## Underlying Base Algorithm(s)
The problem can be solved using a brute-force enumeration approach. Since the constraints for this version (Part I) are small ($N \le 50$), we can iterate through all possible start and end indices of subarrays, remove the subarray, and verify if the remaining elements form a strictly increasing sequence.

---

## Complexity Analysis
- **Time Complexity**: $O(N^3)$, where $N$ is the length of the array. We have $O(N^2)$ subarrays, and for each, we perform an $O(N)$ check to verify if the remaining sequence is strictly increasing.
- **Space Complexity**: $O(N)$ to store the remaining elements during the verification process.

# Apply Operations to Maximize Frequency Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2968 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Official Link | [apply-operations-to-maximize-frequency-score](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) |

## Problem Description & Examples
### Goal
Given an array of integers and a budget `k`, you can perform an operation where you increment or decrement any element by 1. The goal is to find the maximum possible frequency of any single value in the array after performing at most `k` operations.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the maximum total number of operations allowed.

**Return value**

- An integer representing the maximum frequency of any element achievable within the operation budget.

### Examples
**Example 1**

- Input: `nums = [1, 4, 8, 13], k = 5`
- Output: `2`
- Explanation: We can change 1 to 4 (3 ops) or 4 to 1 (3 ops), or 8 to 13 (5 ops). Max frequency is 2.

**Example 2**

- Input: `nums = [3, 9, 6], k = 2`
- Output: `1`
- Explanation: No two numbers can be made equal with only 2 operations.

**Example 3**

- Input: `nums = [1, 2, 6, 4], k = 1`
- Output: `3`
- Explanation: Change 1 and 2 to 2 (1 op) or 4 and 6 to 4 (2 ops, too many). Max frequency is 2.

---

## Underlying Base Algorithm(s)
The problem is solved by sorting the array and using a sliding window approach combined with prefix sums. For any subarray of length `L`, the cost to make all elements equal to the median element is minimized. The prefix sum array allows us to calculate the cost to transform all elements in a window `[i, j]` to the median `nums[(i+j)//2]` in O(1) time. We use a sliding window to find the largest window size that satisfies the cost constraint `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the initial sorting of the array. The sliding window traversal takes `O(n)`.
- **Space Complexity**: `O(n)` to store the prefix sum array.

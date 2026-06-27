# Minimum Operations to Make Elements Within K Subarrays Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3505 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Dynamic Programming, Sliding Window, Heap (Priority Queue) |
| Official Link | [minimum-operations-to-make-elements-within-k-subarrays-equal](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, determine the minimum number of operations required to make all elements within every possible subarray of length `k` equal to the same value. An operation consists of incrementing or decrementing any element in the array by 1. Since every element must eventually belong to a subarray of length `k` where all elements are equal, this effectively implies that the entire array must be transformed into a sequence where every window of size `k` has identical elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the size of the sliding window.

**Return value**

- An integer representing the minimum total operations (sum of absolute differences) to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `2`
- Explanation: We can change the array to `[2, 2, 2]`. Operations: |1-2| + |3-2| = 2.

**Example 2**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `0`
- Explanation: The array already satisfies the condition.

**Example 3**

- Input: `nums = [1, 10, 1], k = 2`
- Output: `9`
- Explanation: We can change the array to `[1, 1, 1]`. Operations: |10-1| = 9.

---

## Underlying Base Algorithm(s)
The problem relies on the property that to minimize the sum of absolute differences $\sum |x_i - target|$, the optimal `target` is the **median** of the set of numbers. Since the constraint requires every window of size `k` to have equal elements, this implies that $nums[i] = nums[i+k]$ for all valid $i$. We can decompose the array into $k$ independent groups based on indices modulo $k$. For each group, we find the median and calculate the cost to transform all elements in that group to the median.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the array, due to sorting each of the $k$ groups.
- **Space Complexity**: $O(n)$ to store the partitioned groups.

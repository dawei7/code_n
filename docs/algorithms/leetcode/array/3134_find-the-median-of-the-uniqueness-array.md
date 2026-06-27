# Find the Median of the Uniqueness Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3134 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [find-the-median-of-the-uniqueness-array](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) |

## Problem Description & Examples
### Goal
Given an integer array, consider all possible contiguous subarrays. For each subarray, calculate the number of distinct elements it contains. The "uniqueness array" is the collection of these distinct counts for every possible subarray, sorted in non-decreasing order. The goal is to find the median value of this uniqueness array. If the total number of subarrays is $N$, the median is the element at index $\lceil N/2 \rceil - 1$ (0-indexed).

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the median value of the uniqueness array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `1`
- Explanation: Subarrays are [1], [2], [3], [1,2], [2,3], [1,2,3]. Distinct counts: 1, 1, 1, 2, 2, 3. Sorted: [1, 1, 1, 2, 2, 3]. Median is at index (6+1)//2 - 1 = 2, which is 1.

**Example 2**

- Input: `nums = [3, 4, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [73, 33, 9]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Binary Search on the Answer** and a **Sliding Window** technique. Since the uniqueness array is monotonic in nature (the count of distinct elements is non-decreasing as we expand subarrays), we can binary search for the smallest value $k$ such that at least $\lceil N/2 \rceil$ subarrays have $\le k$ distinct elements. The sliding window efficiently counts how many subarrays have at most $k$ distinct elements in $O(n)$ time.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the array. The binary search runs in $O(\log n)$ iterations, and each check using the sliding window takes $O(n)$.
- **Space Complexity**: $O(n)$ to store the frequency map used in the sliding window.

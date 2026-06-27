# Count of Smaller Numbers After Self

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 315 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [count-of-smaller-numbers-after-self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |

## Problem Description & Examples
### Goal
Given an integer array, determine for each element how many integers to its right are strictly smaller than it. The result should be an array where the value at each index corresponds to this count.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the count of smaller elements to the right for each corresponding input element.

### Examples
**Example 1**

- Input: `nums = [5, 2, 6, 1]`
- Output: `[2, 1, 1, 0]`

**Example 2**

- Input: `nums = [-1]`
- Output: `[0]`

**Example 3**

- Input: `nums = [-1, -1]`
- Output: `[0, 0]`

---

## Underlying Base Algorithm(s)
The problem is efficiently solved using a Fenwick Tree (Binary Indexed Tree) or a modified Merge Sort. By mapping the input values to their relative ranks (coordinate compression), we can use a Fenwick Tree to track the frequency of elements encountered while traversing the array from right to left. Each query to the Fenwick Tree returns the prefix sum of frequencies, representing the count of smaller elements already processed.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the input array. Coordinate compression takes `O(n log n)`, and each of the `n` insertions/queries in the Fenwick Tree takes `O(log n)`.
- **Space Complexity**: `O(n)` to store the Fenwick Tree and the rank mapping.

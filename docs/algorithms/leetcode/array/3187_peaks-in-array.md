# Peaks in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3187 |
| Difficulty | Hard |
| Topics | Array, Binary Indexed Tree, Segment Tree |
| Official Link | [peaks-in-array](https://leetcode.com/problems/peaks-in-array/) |

## Problem Description & Examples
### Goal
The objective is to maintain an array of integers and perform two types of operations efficiently: updating the value of an element at a specific index and querying the number of "peaks" within a given range `[l, r]`. A peak is defined as an element that is strictly greater than its immediate neighbors (indices `i-1` and `i+1`). Note that the first and last elements of the array cannot be peaks.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `queries`: A list of queries, where each query is either `[1, l, r]` (count peaks in range `[l, r]`) or `[2, index, val]` (update `nums[index]` to `val`).

**Return value**

- A list of integers containing the results of all range count queries.

### Examples
**Example 1**

- Input: `nums = [3, 1, 4, 2, 5], queries = [[2, 3, 4], [1, 0, 4]]`
- Output: `[0]`
- Explanation: After updating index 3 to 4, the array becomes `[3, 1, 4, 4, 5]`. No element is strictly greater than both neighbors.

**Example 2**

- Input: `nums = [4, 1, 4, 2, 1, 5], queries = [[2, 2, 4], [1, 0, 2], [1, 0, 5]]`
- Output: `[1, 1]`

**Example 3**

- Input: `nums = [5, 4, 8, 6], queries = [[1, 2, 2], [1, 1, 2], [2, 1, 6], [1, 0, 3]]`
- Output: `[0, 0, 1]`

---

## Underlying Base Algorithm(s)
The problem requires point updates and range sum queries. A Binary Indexed Tree (BIT) or Fenwick Tree is ideal here. We maintain a BIT where an index `i` stores `1` if `nums[i]` is a peak, and `0` otherwise. Since a change at index `i` only affects whether `i-1`, `i`, and `i+1` are peaks, we perform a constant number of updates to the BIT for each array modification.

---

## Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`, where `N` is the length of the array and `Q` is the number of queries. Each update and query operation takes `O(log N)` time.
- **Space Complexity**: `O(N)` to store the array and the Binary Indexed Tree.

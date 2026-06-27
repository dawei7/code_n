# Count Substrings That Satisfy K-Constraint II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3261 |
| Difficulty | Hard |
| Topics | Array, String, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [count-substrings-that-satisfy-k-constraint-ii](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/) |

## Problem Description & Examples
### Goal
Given a binary string `s` and an integer `k`, determine the number of substrings within specified ranges `[l, r]` that satisfy the "k-constraint." A substring satisfies the k-constraint if the count of '0's is at most `k` OR the count of '1's is at most `k`. For multiple queries, efficiently calculate the total count of valid substrings contained entirely within each query range.

### Function Contract
**Inputs**

- `s`: A string consisting of characters '0' and '1'.
- `k`: An integer representing the maximum allowed frequency of either '0's or '1's.
- `queries`: A 2D list where each element `[l, r]` defines the start and end indices of a substring range.

**Return value**

- A list of integers where each element corresponds to the count of valid substrings for the respective query.

### Examples
**Example 1**

- Input: `s = "0001111", k = 2, queries = [[0, 6]]`
- Output: `[26]`

**Example 2**

- Input: `s = "010101", k = 1, queries = [[0, 7], [2, 3], [0, 3]]`
- Output: `[15, 3, 6]`

**Example 3**

- Input: `s = "11111", k = 1, queries = [[0, 4]]`
- Output: `[9]`

---

## Underlying Base Algorithm(s)
The solution utilizes a **Sliding Window** to precompute the leftmost valid starting index `left[i]` for every position `i` in the string. By using **Prefix Sums** on the lengths of valid substrings ending at each index, we can answer range queries in constant time. Specifically, for a query `[L, R]`, we identify the valid range `[start, end]` and calculate the sum of valid substrings using the precomputed prefix array.

---

## Complexity Analysis
- **Time Complexity**: `O(n + q)`, where `n` is the length of the string and `q` is the number of queries. The sliding window takes `O(n)`, and each query is answered in `O(1)`.
- **Space Complexity**: `O(n)` to store the `left` boundary array and the prefix sum array.

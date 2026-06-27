# Maximum Strong Pair XOR II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2935 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Bit Manipulation, Trie, Sliding Window |
| Official Link | [maximum-strong-pair-xor-ii](https://leetcode.com/problems/maximum-strong-pair-xor-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify all "strong pairs" (x, y) such that the absolute difference between the two numbers is less than or equal to the smaller of the two (i.e., |x - y| ≤ min(x, y)). Among all such pairs, determine the maximum possible value of the bitwise XOR operation (x ^ y).

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the maximum XOR value achievable by any strong pair in the input array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `7`
- Explanation: Strong pairs include (2, 3) where |2-3| <= 2, (4, 5) where |4-5| <= 4, etc. The max XOR is 3 ^ 5 = 6, or 2 ^ 5 = 7.

**Example 2**

- Input: `nums = [10, 20]`
- Output: `0`
- Explanation: |10 - 20| = 10. min(10, 20) = 10. Since 10 <= 10, (10, 20) is a strong pair. 10 ^ 20 = 30.

**Example 3**

- Input: `nums = [5, 6, 25, 30]`
- Output: `7`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Trie (Prefix Tree)** combined with a **Sliding Window** approach. By sorting the array, the condition `|x - y| <= min(x, y)` simplifies to `y <= 2 * x` (assuming `x <= y`). As we iterate through the sorted array with a pointer `y`, we maintain a sliding window of valid `x` values in the Trie. We remove elements from the Trie that no longer satisfy the condition as `y` increases, and query the Trie for the value that maximizes the XOR with the current `y`.

---

## Complexity Analysis
- **Time Complexity**: `O(N * log(max(nums)))`, where `N` is the length of the array. Sorting takes `O(N log N)`, and for each element, we perform constant-time Trie insertions and queries proportional to the number of bits (approx. 20).
- **Space Complexity**: `O(N * log(max(nums)))` to store the Trie nodes.

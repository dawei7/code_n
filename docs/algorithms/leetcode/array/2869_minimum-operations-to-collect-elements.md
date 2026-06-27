# Minimum Operations to Collect Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2869 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [minimum-operations-to-collect-elements](https://leetcode.com/problems/minimum-operations-to-collect-elements/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, determine the minimum number of elements that must be removed from the end of the array to collect all integers from 1 to `k` inclusive.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence.
- `k`: An integer representing the target range of values [1, k] to collect.

**Return value**

- An integer representing the minimum number of operations (removals from the end) required to gather all integers in the set {1, 2, ..., k}.

### Examples
**Example 1**

- Input: `nums = [3, 1, 5, 4, 2], k = 2`
- Output: `4`
- Explanation: Removing 2, 4, 5, 1 leaves {3, 1}. We have collected 1 and 2.

**Example 2**

- Input: `nums = [3, 1, 5, 4, 2], k = 5`
- Output: `5`

**Example 3**

- Input: `nums = [3, 2, 5, 3, 1], k = 3`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using a reverse iteration approach combined with a Hash Set (or a boolean array) to track unique collected elements. By traversing the array from right to left, we can greedily identify the first occurrence of each number in the range [1, k]. Once the size of our tracking set reaches `k`, the current index provides the total count of operations.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array at most once.
- **Space Complexity**: `O(k)`, as we store at most `k` unique integers in our tracking set.

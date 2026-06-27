# Sorting Three Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2826 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming |
| Official Link | [sorting-three-groups](https://leetcode.com/problems/sorting-three-groups/) |

## Problem Description & Examples
### Goal
Given an array of integers where each element is either 1, 2, or 3, determine the minimum number of elements that must be moved (or changed) to make the entire array non-decreasing. Since we only care about the relative order of 1s, 2s, and 3s, this is equivalent to finding the Longest Non-Decreasing Subsequence of the array and subtracting its length from the total number of elements.

### Function Contract
**Inputs**

- `nums`: A list of integers where each integer is 1, 2, or 3.

**Return value**

- An integer representing the minimum number of operations required to sort the array in non-decreasing order.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 2, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 3, 2, 1, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [2, 2, 2, 2, 3, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain the state of the minimum operations required to end in a non-decreasing sequence ending with a 1, 2, or 3. Alternatively, this can be solved by finding the Longest Non-Decreasing Subsequence (LNDS) using the property that the sequence must consist of a block of 1s, followed by a block of 2s, followed by a block of 3s.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once.
- **Space Complexity**: `O(1)`, as we only store the counts for the three possible ending states.

# Sum of Imbalance Numbers of All Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2763 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Enumeration |
| Official Link | [sum-of-imbalance-numbers-of-all-subarrays](https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/) |

## Problem Description & Examples
### Goal
Calculate the total "imbalance number" across every possible contiguous subarray of a given integer array. The imbalance number of a sequence is defined as the count of elements `x` such that `x + 1` is not present in the sequence, excluding the minimum element of that sequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 ≤ nums[i] ≤ n.

**Return value**

- An integer representing the sum of imbalance numbers for all contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [2, 3, 1]`
- Output: `0`
- Explanation: Subarrays are [2], [3], [1], [2,3], [3,1], [2,3,1]. All have an imbalance of 0.

**Example 2**

- Input: `nums = [1, 3, 3]`
- Output: `1`
- Explanation: The subarray [1, 3] has an imbalance of 1 because 2 is missing.

**Example 3**

- Input: `nums = [4, 5, 6, 1, 2]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved by iterating through all possible starting positions `i` of a subarray and expanding to the right `j`. As we expand, we maintain a set of seen numbers to track the imbalance. Specifically, when adding a number `x`, we check if `x-1` and `x+1` are already in the set to update the imbalance count dynamically.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the input array, as we iterate through all subarrays.
- **Space Complexity**: `O(n)` to store the set of elements present in the current subarray.

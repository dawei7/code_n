# Maximize Consecutive Elements in an Array After Modification

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3041 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [maximize-consecutive-elements-in-an-array-after-modification](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/) |

## Problem Description & Examples
### Goal
Given an array of integers, you are permitted to increment each element by at most 1. The objective is to select a subset of these modified elements such that they form the longest possible sequence of consecutive integers (e.g., `x, x+1, x+2, ...`). Determine the maximum length of such a sequence.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum length of a consecutive sequence that can be formed after modifying each element by at most 1.

### Examples
**Example 1**

- Input: `nums = [2, 1, 5, 1, 1]`
- Output: `3`
- Explanation: We can modify the array to `[2, 1, 6, 2, 2]`. Selecting `[1, 2, 2]` (or similar) allows forming a sequence of length 3.

**Example 2**

- Input: `nums = [1, 4, 7, 10]`
- Output: `1`
- Explanation: No consecutive sequence longer than 1 can be formed.

**Example 3**

- Input: `nums = [8, 4, 5, 10, 7]`
- Output: `4`
- Explanation: By modifying elements, we can form the sequence `[4, 5, 7, 8]` (after adjustments).

---

## Underlying Base Algorithm(s)
The problem is solved using **Sorting** combined with **Dynamic Programming**. By sorting the array first, we can process elements in increasing order. We maintain a dictionary (or hash map) to store the length of the longest consecutive sequence ending at a specific value `v`. For each number `x` in the sorted array, we can either use `x` or `x+1`. We update the DP state based on the values `x` and `x+1` to track the maximum sequence length found so far.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the initial sorting of the input array, where `N` is the length of the array. The subsequent linear scan and dictionary lookups take `O(N)`.
- **Space Complexity**: `O(N)` to store the DP state in a dictionary.

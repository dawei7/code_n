# Minimum Swaps to Sort by Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3551 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting |
| Official Link | [minimum-swaps-to-sort-by-digit-sum](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the minimum number of swaps required to sort the array such that elements are ordered primarily by the sum of their digits (in non-decreasing order). If two numbers have the same digit sum, their relative order should be preserved based on their original indices (stable sort behavior).

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the minimum number of swaps required to reach the target sorted state.

### Examples
**Example 1**

- Input: `nums = [13, 22, 31]`
- Output: `0`
- Explanation: Digit sums are 4, 4, 4. They are already in stable order.

**Example 2**

- Input: `nums = [15, 8, 2]`
- Output: `1`
- Explanation: Digit sums are 6, 8, 2. Sorted order of sums: 2, 6, 8. Target array: [2, 15, 8]. One swap (15 and 2) achieves this.

**Example 3**

- Input: `nums = [10, 20, 30]`
- Output: `0`
- Explanation: Digit sums are 1, 2, 3. Already sorted.

---

## Underlying Base Algorithm(s)
The problem is solved by first determining the target permutation of the array indices based on the custom sorting criteria (digit sum, then original index). Once the target positions are known, the problem reduces to finding the minimum number of swaps to transform the current permutation into the target permutation. This is equivalent to counting the number of cycles in the permutation graph: `swaps = N - number_of_cycles`.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where `N` is the length of the array. The cycle decomposition takes `O(N)`.
- **Space Complexity**: `O(N)` to store the target indices and the visited array for cycle detection.

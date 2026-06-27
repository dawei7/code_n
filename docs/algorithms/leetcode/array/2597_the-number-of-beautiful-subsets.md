# The Number of Beautiful Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2597 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Sorting, Combinatorics |
| Official Link | [the-number-of-beautiful-subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/) |

## Problem Description & Examples
### Goal
Given an array of integers and a positive integer `k`, determine the total number of non-empty subsets of the array such that no two elements in the subset have an absolute difference exactly equal to `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available elements.
- `k`: An integer representing the forbidden absolute difference.

**Return value**

- An integer representing the count of all valid non-empty subsets.

### Examples
**Example 1**

- Input: `nums = [2,4,6], k = 2`
- Output: `4`
- Explanation: The valid subsets are [2], [4], [6], [2, 6].

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `1`
- Explanation: The only valid subset is [1].

**Example 3**

- Input: `nums = [10,4,5,7,2,1], k = 3`
- Output: `23`

---

## Underlying Base Algorithm(s)
The problem is solved using Backtracking with pruning. By sorting the array, we can process elements and decide whether to include them in the current subset based on whether their inclusion violates the condition (i.e., if `x - k` is already present in the current subset). Alternatively, this can be modeled as a combinatorial problem by grouping numbers into chains based on their values modulo `k` and using dynamic programming to count valid combinations within each chain.

---

## Complexity Analysis
- **Time Complexity**: O(2^n) in the worst case for backtracking, where n is the length of the array. With optimization (grouping by modulo), it can be reduced to O(n log n) due to sorting.
- **Space Complexity**: O(n) to store the recursion stack and the frequency map of the current subset.

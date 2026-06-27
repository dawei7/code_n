# Minimize the Maximum Difference of Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2616 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Sorting |
| Official Link | [minimize-the-maximum-difference-of-pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `p`, the objective is to form `p` disjoint pairs of elements from the array such that the maximum absolute difference between the two elements in any of the pairs is minimized. Return this minimized maximum difference.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available numbers.
- `p`: An integer representing the number of pairs to be formed.

**Return value**

- An integer representing the smallest possible value for the maximum difference among all `p` pairs.

### Examples
**Example 1**

- Input: `nums = [10,1,2,7,1,3], p = 2`
- Output: `1`
- Explanation: We can form pairs (1, 1) and (2, 3). The differences are 0 and 1. The maximum is 1.

**Example 2**

- Input: `nums = [4,2,1,2], p = 1`
- Output: `0`
- Explanation: We can form the pair (2, 2). The difference is 0.

**Example 3**

- Input: `nums = [3,4,2,3,2,1,2], p = 3`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the possible difference ranges from 0 to the maximum possible difference in the array, we can binary search for the smallest threshold `x` such that it is possible to form at least `p` pairs where each pair has a difference ≤ `x`. A **Greedy** approach is used within the binary search check function: after sorting the array, we iterate through it and greedily pick adjacent elements if their difference is within the current threshold.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + N log D)`, where `N` is the length of the array and `D` is the range of the maximum difference (max(nums) - min(nums)). Sorting takes `O(N log N)`, and the binary search performs `O(log D)` checks, each taking `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.

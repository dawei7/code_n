# Increasing Triplet Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 334 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [increasing-triplet-subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) |

## Problem Description & Examples
### Goal
Determine if there exists a triplet of indices $(i, j, k)$ such that $i < j < k$ and the values at these indices satisfy $nums[i] < nums[j] < nums[k]$. The function should return a boolean indicating whether such a subsequence exists in the given array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- `bool`: `True` if an increasing triplet exists, `False` otherwise.

### Examples
**Example 1**

- Input: `[1, 2, 3, 4, 5]`
- Output: `True`

**Example 2**

- Input: `[5, 4, 3, 2, 1]`
- Output: `False`

**Example 3**

- Input: `[2, 1, 5, 0, 4, 6]`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. We maintain two variables, `first` and `second`, representing the smallest and second-smallest values encountered so far that could potentially form the first two elements of an increasing triplet. As we iterate through the array, if we find a number greater than `second`, we have successfully found a triplet.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we perform a single pass through the data.
- **Space Complexity**: $O(1)$, as we only use two variables to track the state regardless of the input size.

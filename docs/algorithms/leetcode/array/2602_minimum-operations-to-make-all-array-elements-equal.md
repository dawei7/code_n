# Minimum Operations to Make All Array Elements Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2602 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting, Prefix Sum |
| Official Link | [minimum-operations-to-make-all-array-elements-equal](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/) |

## Problem Description & Examples
### Goal
Given an array of integers and a list of target values, calculate the total number of operations required to make every element in the array equal to each target value. An operation consists of incrementing or decrementing an element by 1. For each target, return the sum of absolute differences between the target and every element in the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `queries`: A list of integers where each integer is a target value.

**Return value**

- A list of integers representing the total operations needed for each query.

### Examples
**Example 1**

- Input: `nums = [3,1,6,8], queries = [1,5]`
- Output: `[14,10]`

**Example 2**

- Input: `nums = [2,9,6,3], queries = [10]`
- Output: `[20]`

**Example 3**

- Input: `nums = [1], queries = [0]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The problem is solved by sorting the input array and utilizing prefix sums to calculate the sum of elements in $O(1)$ time. For each query, we use binary search (`bisect_left`) to partition the array into elements smaller than the target and elements greater than or equal to the target. The cost is calculated as: `(target * count_smaller - sum_smaller) + (sum_larger - target * count_larger)`.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N + Q \log N)$, where $N$ is the length of `nums` and $Q$ is the length of `queries`. Sorting takes $O(N \log N)$, and each of the $Q$ queries takes $O(\log N)$ for binary search.
- **Space Complexity**: $O(N)$ to store the prefix sum array.

# Frequency of the Most Frequent Element

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) |
| Frontend ID | 1838 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The frequency of a value is its number of occurrences in an array. You are given a positive integer array `nums` and a budget `k`. One operation chooses one array index and increases its value by exactly 1.

Perform at most `k` operations and return the greatest frequency that any single value can have afterward. Operations may be distributed among different elements, but values can only increase; decreasing a larger value to join a smaller target is not allowed.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: the maximum total number of unit increments, where $1 \le k \le 10^5$.

**Return value**

- Return the maximum achievable occurrence count of one value after using at most `k` increments.

### Examples

**Example 1**

- Input: `nums = [1,2,4], k = 5`
- Output: `3`

Raise 1 by three and 2 by two, producing three copies of 4.

**Example 2**

- Input: `nums = [1,4,8,13], k = 5`
- Output: `2`

Several pairs can be equalized, but no three values fit the budget.

**Example 3**

- Input: `nums = [3,9,6], k = 2`
- Output: `1`

Every gap between different values exceeds the available operations.

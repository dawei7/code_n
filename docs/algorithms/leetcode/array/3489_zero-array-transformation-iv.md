# Zero Array Transformation IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3489 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [zero-array-transformation-iv](https://leetcode.com/problems/zero-array-transformation-iv/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and a set of queries, each defined by a range `[l, r]`, determine the minimum number of queries (from the start of the query list) required to reduce all elements in `nums` to zero. Each query `[l, r]` allows you to decrement all elements in the range `[l, r]` by 1, provided the element is greater than 0. If it is impossible to reduce all elements to zero even after using all queries, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial state of the array.
- `queries`: A list of lists, where each `queries[i]` is `[l, r]` representing the range affected by the $i$-th query.

**Return value**

- An integer representing the minimum prefix of `queries` needed to make all elements in `nums` zero, or -1 if it is impossible.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2], queries = [[0, 2], [1, 2], [0, 2]]`
- Output: `2`

**Example 2**

- Input: `nums = [4, 3, 2, 1], queries = [[1, 3], [0, 2]]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 1, 1], queries = [[0, 0], [1, 1], [2, 2]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of **Binary Search on the Answer** and the **Difference Array (Sweep Line)** technique. Since the ability to zero out the array is monotonic (if $k$ queries work, $k+1$ queries also work), we binary search for the smallest $k$. For a fixed $k$, we use a difference array to calculate the total decrement applied to each index in $O(n + k)$ time, then verify if every `nums[i]` is less than or equal to the total decrement applied at that index.

## Complexity Analysis
- **Time Complexity**: $O((n + q) \log q)$, where $n$ is the length of `nums` and $q$ is the number of queries. The binary search runs $\log q$ times, and each check takes $O(n + q)$.
- **Space Complexity**: $O(n)$, required for the difference array used during the verification step.

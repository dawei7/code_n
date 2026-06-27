# Beautiful Towers II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2866 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [beautiful-towers-ii](https://leetcode.com/problems/beautiful-towers-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers representing the maximum allowed heights of towers at each index, construct a "mountain" configuration. A mountain configuration is defined as a sequence of heights where there exists a peak index `i` such that heights increase up to `i` and decrease thereafter. The heights must satisfy the constraint that each tower `j` has a height `h[j] <= maxHeights[j]`. The objective is to find the maximum possible sum of heights for any valid mountain configuration.

### Function Contract
**Inputs**

- `maxHeights`: A list of integers representing the upper bound for the height of each tower.

**Return value**

- An integer representing the maximum possible sum of heights of a mountain-shaped configuration.

### Examples
**Example 1**

- Input: `maxHeights = [5, 3, 4, 1, 1]`
- Output: `13`

**Example 2**

- Input: `maxHeights = [6, 5, 3, 9, 2, 7]`
- Output: `22`

**Example 3**

- Input: `maxHeights = [3, 2, 5, 5, 2, 3]`
- Output: `18`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Monotonic Stack**. By calculating the prefix sums of the maximum possible heights to the left of each index (where heights are non-decreasing) and the suffix sums to the right (where heights are non-increasing), we can determine the total sum for a peak at any index `i` in $O(1)$ time after $O(n)$ preprocessing. The monotonic stack helps find the nearest smaller element to the left and right efficiently.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of `maxHeights`. We perform a constant number of linear passes over the array using the stack.
- **Space Complexity**: $O(n)$ to store the prefix/suffix sum arrays and the monotonic stack.

# Beautiful Towers I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2865 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [beautiful-towers-i](https://leetcode.com/problems/beautiful-towers-i/) |

## Problem Description & Examples
### Goal
Given an array of maximum heights for a sequence of towers, determine the maximum possible sum of heights for a "beautiful" configuration. A configuration is beautiful if there exists a peak index `i` such that heights are non-decreasing up to `i` and non-increasing after `i`, with every tower's height being at most its corresponding maximum height limit.

### Function Contract
**Inputs**

- `maxHeights`: A list of integers representing the upper bound for the height of each tower at index `i`.

**Return value**

- An integer representing the maximum possible sum of heights of a beautiful tower configuration.

### Examples
**Example 1**

- Input: `maxHeights = [5,3,4,1,1]`
- Output: `13`

**Example 2**

- Input: `maxHeights = [6,5,3,9,2,7]`
- Output: `22`

**Example 3**

- Input: `maxHeights = [3,2,5,5,2,3]`
- Output: `18`

---

## Underlying Base Algorithm(s)
The problem can be solved by iterating through every possible index `i` as the peak of the mountain. For each `i`, we calculate the sum of heights by greedily extending non-decreasingly to the left and non-increasingly to the right. While this brute-force approach is $O(n^2)$ and sufficient for the constraints of "Beautiful Towers I", the problem can be optimized to $O(n)$ using a monotonic stack to precompute the sum of heights for all possible peaks.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$ for the brute-force approach, where $n$ is the number of towers.
- **Space Complexity**: $O(1)$ additional space (excluding the input array).

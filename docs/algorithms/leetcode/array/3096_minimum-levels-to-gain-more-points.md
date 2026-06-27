# Minimum Levels to Gain More Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3096 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [minimum-levels-to-gain-more-points](https://leetcode.com/problems/minimum-levels-to-gain-more-points/) |

## Problem Description & Examples
### Goal
Given an array of game levels where each level is represented by 1 (win) or 0 (loss), determine the minimum number of levels the first player must complete to ensure their total score is strictly greater than the second player's total score. The game must be split into two non-empty parts, where the first player takes the first $k$ levels and the second player takes the remaining levels. If no such split exists, return -1.

### Function Contract
**Inputs**

- `possible`: A list of integers where each element is either 0 or 1.

**Return value**

- An integer representing the minimum number of levels (1-indexed) the first player must play, or -1 if it is impossible to achieve a higher score than the second player.

### Examples
**Example 1**

- Input: `possible = [1, 0, 1, 0]`
- Output: `1`

**Example 2**

- Input: `possible = [1, 1, 1, 1, 1]`
- Output: `3`

**Example 3**

- Input: `possible = [0, 0]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Prefix Sum** technique. By pre-calculating the total sum of the array, we can determine the second player's score in constant time for any given split point. We iterate through the array once, maintaining a running sum for the first player and subtracting that from the total sum to find the second player's score, checking the condition at each step.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array. We perform one pass to calculate the total sum and a second pass to evaluate the split points.
- **Space Complexity**: $O(1)$, as we only use a few integer variables to track the running sums and the total sum.

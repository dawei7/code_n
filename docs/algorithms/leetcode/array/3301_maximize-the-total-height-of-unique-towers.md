# Maximize the Total Height of Unique Towers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3301 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximize-the-total-height-of-unique-towers](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/) |

## Problem Description & Examples
### Goal
Given an array of maximum allowed heights for a set of towers, assign each tower a height such that all assigned heights are unique and each height is less than or equal to its corresponding maximum limit. The objective is to maximize the sum of all assigned heights. If it is impossible to assign unique heights under the given constraints, return -1.

### Function Contract
**Inputs**

- `maximumHeight`: A list of integers representing the upper bound for each tower's height.

**Return value**

- An integer representing the maximum possible sum of heights, or -1 if no valid assignment exists.

### Examples
**Example 1**

- Input: `maximumHeight = [2, 3, 4, 3]`
- Output: `10`
- Explanation: We can assign heights [2, 3, 4, 1]. The sum is 10.

**Example 2**

- Input: `maximumHeight = [15, 15]`
- Output: `29`
- Explanation: We can assign heights [15, 14]. The sum is 29.

**Example 3**

- Input: `maximumHeight = [2, 2, 2]`
- Output: `-1`
- Explanation: It is impossible to assign unique heights because we only have one available height (2) that is less than or equal to the maximums.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the maximum heights in descending order, we can greedily assign the largest possible valid height to each tower. For each tower, we pick the minimum of its allowed maximum height and the height assigned to the previous tower minus one.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting of the input array, where N is the number of towers. The subsequent linear pass is `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.

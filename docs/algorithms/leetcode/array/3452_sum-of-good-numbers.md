# Sum of Good Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3452 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [sum-of-good-numbers](https://leetcode.com/problems/sum-of-good-numbers/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, identify all "good" numbers in the array. A number at index `i` is considered "good" if it is strictly greater than the elements at both index `i - k` and `i + k` (if those indices exist within the array bounds). The objective is to return the sum of all such good numbers.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the offset distance to check neighbors.

**Return value**

- An integer representing the sum of all elements that satisfy the "good" condition.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 1, 5, 4], k = 2`
- Output: `12`
- Explanation: 3 is greater than 1 and 1 (indices 0 and 4), 5 is greater than 2 and 4 (indices 2 and 6 - wait, index 4 is 5, neighbors are 2 and 4). 3 + 5 + 4 = 12.

**Example 2**

- Input: `nums = [2, 1], k = 1`
- Output: `2`
- Explanation: 2 is greater than 1 (index 1).

**Example 3**

- Input: `nums = [3, 8, 6, 4, 1], k = 2`
- Output: `14`
- Explanation: 8 is greater than 3 and 4. 6 is greater than 8 (False). 6 is greater than 1. 8 + 6 = 14.

---

## Underlying Base Algorithm(s)
Linear scan (Iteration). The problem requires a single pass through the array to evaluate the condition for each element based on its relative neighbors at distance `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a single variable to accumulate the sum.

# Number of Ways to Earn Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2585 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [number-of-ways-to-earn-points](https://leetcode.com/problems/number-of-ways-to-earn-points/) |

## Problem Description & Examples
### Goal
Given a target total score and a list of available question types, where each type has a specific point value and a limited count of questions available, determine the total number of distinct ways to achieve exactly the target score. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `target`: An integer representing the exact score to reach.
- `types`: A list of lists, where each inner list `[count_i, marks_i]` indicates that there are `count_i` questions available, each worth `marks_i` points.

**Return value**

- An integer representing the number of ways to reach the target score, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `target = 6, types = [[6,1],[3,2],[2,3]]`
- Output: `7`

**Example 2**

- Input: `target = 5, types = [[50,1],[50,2],[50,5]]`
- Output: `4`

**Example 3**

- Input: `target = 18, types = [[6,1],[3,2],[2,3]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
This problem is a variation of the **Bounded Knapsack Problem**. It can be solved using **Dynamic Programming** with a 1D array (space-optimized) or a 2D array. We maintain a DP table where `dp[s]` represents the number of ways to achieve score `s`. For each question type, we update the DP table by considering taking 0 to `count_i` questions of that type.

---

## Complexity Analysis
- **Time Complexity**: O(target * N * max(count_i)), where N is the number of question types. This can be optimized to O(target * N) using prefix sums or sliding window techniques to update the DP table.
- **Space Complexity**: O(target) to store the number of ways to reach each score up to the target.

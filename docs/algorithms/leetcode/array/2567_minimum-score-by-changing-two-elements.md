# Minimum Score by Changing Two Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2567 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-score-by-changing-two-elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements/) |

## Problem Description & Examples
### Goal
Given an array of integers, you are allowed to modify exactly two elements to any integer value of your choice. The objective is to minimize the "low-high score," defined as the difference between the maximum and minimum values in the array after performing these two modifications.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where the length is at least 3.

**Return value**

- An integer representing the minimum possible difference between the maximum and minimum elements after changing at most two elements.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3]`
- Output: `0`
- Explanation: Change 1 and 4 to 3. The array becomes [3, 3, 3], max - min = 0.

**Example 2**

- Input: `nums = [1, 4, 7, 8, 5]`
- Output: `3`
- Explanation: Change 7 and 8 to 5. The array becomes [1, 4, 5, 5, 5], max - min = 4. Alternatively, change 1 and 8 to 5, array becomes [5, 4, 7, 5, 5], max - min = 3.

**Example 3**

- Input: `nums = [1, 50, 75, 100]`
- Output: `25`
- Explanation: Change 1 and 100 to 50 and 75 respectively. The array becomes [50, 50, 75, 75], max - min = 25.

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy approach combined with Sorting. Since we want to minimize the range (max - min), we should focus on removing the extreme values (the smallest and largest elements). By sorting the array, we can evaluate the three optimal strategies:
1. Remove the two largest elements.
2. Remove the two smallest elements.
3. Remove one smallest and one largest element.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting step, where N is the length of the input array.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.

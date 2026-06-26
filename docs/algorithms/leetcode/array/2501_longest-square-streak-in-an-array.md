# Longest Square Streak in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2501 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Official Link | [longest-square-streak-in-an-array](https://leetcode.com/problems/longest-square-streak-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the length of the longest subsequence such that each element (starting from the second) is the square of the previous element. A streak must contain at least two elements to be considered valid. If no such streak exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where $2 \le nums.length \le 10^5$ and $2 \le nums[i] \le 10^5$.

**Return value**

- An integer representing the length of the longest square streak, or -1 if the maximum streak length is less than 2.

### Examples
**Example 1**

- Input: `nums = [4, 3, 6, 16, 8, 2]`
- Output: `3`
- Explanation: The streak is [2, 4, 16].

**Example 2**

- Input: `nums = [2, 3, 5, 6, 7]`
- Output: `-1`
- Explanation: No square streak exists.

**Example 3**

- Input: `nums = [10, 2, 4, 16, 256]`
- Output: `4`
- Explanation: The streak is [2, 4, 16, 256].

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Set for $O(1)$ average-time lookups. By sorting the array or using a set, we can iterate through each number and greedily calculate the length of the streak starting at that number by repeatedly squaring it and checking for existence in the set. To optimize, we only initiate a streak calculation if the square root of the current number is not present in the set, ensuring each streak is processed exactly once.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$ if sorting is used, or $O(N \log (\max(nums)))$ if using a hash set, where $N$ is the number of elements. Since the maximum value is $10^5$, the number of squares is limited to $\approx \log(\log(10^5))$, making the inner loop effectively constant.
- **Space Complexity**: $O(N)$ to store the elements in a hash set for efficient lookup.

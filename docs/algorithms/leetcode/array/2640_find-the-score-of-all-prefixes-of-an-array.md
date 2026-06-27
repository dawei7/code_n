# Find the Score of All Prefixes of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2640 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [find-the-score-of-all-prefixes-of-an-array](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the "score" for every prefix of the array. The score of a prefix is defined as the sum of the "converted" elements of that prefix. An element is converted by adding the current element to the maximum value encountered in the prefix up to that point. The final output is an array where each index `i` contains the cumulative score of the prefix ending at `i`.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the score of each prefix.

### Examples
**Example 1**

- Input: `nums = [2, 3, 7, 6, 1]`
- Output: `[4, 10, 24, 36, 42]`

**Example 2**

- Input: `nums = [1, 1, 2, 4, 8, 16]`
- Output: `[2, 4, 8, 16, 32, 64]`

**Example 3**

- Input: `nums = [10, 2, 5, 1]`
- Output: `[20, 22, 32, 34]`

---

## Underlying Base Algorithm(s)
The problem utilizes a **Prefix Sum** approach combined with **Running Maximum** tracking. By maintaining the maximum value seen so far as we iterate through the array, we can compute the converted value for each index in constant time and accumulate these values to form the prefix score.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(n)` to store the resulting array of scores.

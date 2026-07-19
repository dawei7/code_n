# Relative Ranks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 506 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/relative-ranks/) |

## Problem Description
### Goal
Given the unique competition scores in array `score`, rank athletes in decreasing score order: the highest score has rank 1, the next highest rank 2, and so on. Athlete identity remains the original array index even though ranking is determined by sorted scores.

Return one label for every athlete in original input order. Use `"Gold Medal"`, `"Silver Medal"`, and `"Bronze Medal"` for ranks 1, 2, and 3 respectively; for every later rank, use its decimal string. Preserve all athletes and do not return the scores themselves or reorder the result by placement.

### Function Contract
**Inputs**

- `score`: an array of distinct positive integer scores, one per athlete

**Return value**

- A string array aligned with `score`, containing `"Gold Medal"`, `"Silver Medal"`, `"Bronze Medal"`, or the athlete's numeric rank

### Examples
**Example 1**

- Input: `score = [5, 4, 3, 2, 1]`
- Output: `["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]`

**Example 2**

- Input: `score = [10, 3, 8, 9, 4]`
- Output: `["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]`

**Example 3**

- Input: `score = [1]`
- Output: `["Gold Medal"]`

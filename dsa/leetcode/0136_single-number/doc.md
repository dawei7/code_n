# Single Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 136 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-number/) |

## Problem Description
### Goal
Given a nonempty list of integers, every value occurs exactly twice except for one value that occurs only once. The paired occurrences may appear anywhere in the list and need not be adjacent or ordered.

Return the unique unpaired integer itself, not its position or frequency. Negative values and zero follow the same occurrence rule as positive values, and duplicates should cancel only with an identical value. The input guarantee ensures there is exactly one answer; the intended constraints require processing the list in linear time while using only constant additional storage.

### Function Contract
**Inputs**

- `nums`: integers satisfying the pair-plus-one frequency guarantee

**Return value**

The unique value that occurs once.

### Examples
**Example 1**

- Input: `nums = [4,1,2,1,2]`
- Output: `4`

**Example 2**

- Input: `nums = [2,2,1]`
- Output: `1`

**Example 3**

- Input: `nums = [1]`
- Output: `1`

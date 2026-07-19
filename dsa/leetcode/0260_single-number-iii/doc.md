# Single Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 260 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-number-iii/) |

## Problem Description
### Goal
Given an integer array, exactly two distinct values occur once and every other distinct value occurs exactly twice. Paired occurrences may appear anywhere and need not be adjacent, while the two singleton values may be negative, positive, or zero.

Return the two singleton values in any order, with each appearing once in the result. The task asks for values rather than their indices. Meet the required linear running time and constant extra space instead of sorting the array or storing frequencies for all distinct values, and do not cancel the two different singleton values against each other.

### Function Contract
**Inputs**

- `nums`: an integer array containing exactly two singleton values

**Return value**

The two singleton values in either order.

### Examples
**Example 1**

- Input: `nums = [1,2,1,3,2,5]`
- Output: `[3,5]`

**Example 2**

- Input: `nums = [-1,0]`
- Output: `[-1,0]`

**Example 3**

- Input: `nums = [0,1]`
- Output: `[0,1]`

# Combination Sum IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 377 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-iv/) |

## Problem Description
### Goal
Given unique positive integers `nums` and a positive `target`, build ordered sequences by selecting input values with unlimited reuse. A sequence qualifies when the sum of all selected values equals the target exactly.

Return the number of qualifying sequences. Order matters, so two sequences containing the same multiset in different positions count separately. A target with no valid construction returns zero. Because all choices are positive, extensions strictly increase the running sum. The function returns only the count, not the sequences themselves.

### Function Contract
**Inputs**

- `nums`: a list of distinct positive integers
- `target`: a non-negative target sum

**Return value**

- The number of ordered value sequences summing exactly to `target`.

### Examples
**Example 1**

- Input: `nums = [1,2,3], target = 4`
- Output: `7`

**Example 2**

- Input: `nums = [4], target = 13`
- Output: `0`

**Example 3**

- Input: `nums = [2,5], target = 2`
- Output: `1`

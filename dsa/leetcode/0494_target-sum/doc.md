# Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 494 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/target-sum/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, build an expression by placing exactly one `+` or `-` sign before every array element, keeping the elements in their original order. Evaluate the resulting signed sum after all positions have received a sign.

Return the number of different sign assignments whose expression evaluates to `target`. Choices are attached to array positions, so equal values remain separate decisions; for a zero, `+0` and `-0` are different expressions and must both be counted when valid. The function returns only the number of expressions, not their text or selected sign sequences.

### Function Contract
**Inputs**

- `nums`: a nonempty array of nonnegative integers
- `target`: the desired signed sum

**Return value**

- The number of distinct sign assignments whose value is `target`

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 3`
- Output: `5`

**Example 2**

- Input: `nums = [1], target = 1`
- Output: `1`

**Example 3**

- Input: `nums = [1], target = 2`
- Output: `0`

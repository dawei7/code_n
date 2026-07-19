# Optimal Division

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 553 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/optimal-division/) |

## Problem Description
### Goal
Given an array of positive integers `nums`, insert division operators between every adjacent pair while keeping all values in their original order. Add parentheses wherever needed to choose the evaluation grouping; division uses the represented numerical expression rather than integer truncation.

Return an expression whose value is as large as possible. The string must use every number exactly once and contain no redundant parentheses. For one number, return that number alone; for two numbers, simple division needs no parentheses. When more values are present, grouping denominators differently can change the result even though operand order cannot change.

### Function Contract
**Inputs**

- `nums`: a non-empty list of positive integers

**Return value**

- A string representing a maximum-value division expression

### Examples
**Example 1**

- Input: `nums = [1000, 100, 10, 2]`
- Output: `"1000/(100/10/2)"`

**Example 2**

- Input: `nums = [2]`
- Output: `"2"`

**Example 3**

- Input: `nums = [2, 3]`
- Output: `"2/3"`

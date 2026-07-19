# Biggest Single Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 619 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/biggest-single-number/) |

## Problem Description
### Goal
Given a `MyNumbers` table that may contain duplicate integer values, define a single number as a number that appears exactly once in the entire table. Identify all values meeting that frequency condition.

Return the largest single number in a one-column, one-row result named `num`. If no value appears exactly once, still return one row whose value is `NULL`; do not return an empty result. A numerically large value that appears more than once is not a single number and cannot qualify.

### Function Contract
**Inputs**

- `MyNumbers(num)`: a multiset of integer values

**Return value**

- One column named `num`
- Its value is the maximum integer whose total frequency is one
- If no such integer exists, the query still returns one row containing null

### Examples
**Example 1**

- Input values: `8, 8, 3, 3, 1, 4, 5, 6`
- Output: `6`

**Example 2**

- Input values: `8, 8, 7, 7, 3, 3, 3`
- Output: `null`

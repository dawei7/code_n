# Ones and Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 474 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/ones-and-zeroes/) |

## Problem Description
### Goal
Given binary strings and budgets `m` zeroes and `n` ones, choose a subset of string occurrences. Each selected string consumes resources equal to its own counts of `0` and `1`, and each input position may be selected at most once.

Return the maximum number of strings whose combined zero consumption is at most `m` and combined one consumption is at most `n`. Duplicate strings at different positions are separate choices. Unused budget is allowed, and maximizing total characters is not the objective. The function returns only the largest subset cardinality, not the chosen strings or remaining resources.

### Function Contract
**Inputs**

- `strs`: binary strings, each usable at most once
- `m`: available zero budget
- `n`: available one budget

**Return value**

- The maximum number of selected strings within both budgets

### Examples
**Example 1**

- Input: `strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3`
- Output: `4`

**Example 2**

- Input: `strs = ["10", "0", "1"], m = 1, n = 1`
- Output: `2`

**Example 3**

- Input: `strs = ["0", "0", "1", "1"], m = 2, n = 2`
- Output: `4`

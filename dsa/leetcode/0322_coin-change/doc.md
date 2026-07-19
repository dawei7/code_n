# Coin Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 322 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/coin-change/) |

## Problem Description
### Goal
Given positive integer coin denominations and a nonnegative target `amount`, choose any number of coins whose values sum exactly to the target. Each denomination has an unlimited supply, so it may be selected repeatedly and coin order does not create a different solution.

Return the minimum number of coins among all exact combinations. Return `-1` when no combination can form the amount, and return `0` for amount zero by choosing no coins. A greedy choice of the largest denomination is not guaranteed to be optimal for arbitrary coin systems. The function returns only the minimum count, not the selected denominations.

### Function Contract
**Inputs**

- `coins`: the available positive denominations
- `amount`: the target total

**Return value**

The minimum number of coins whose values sum to `amount`, or `-1` if no combination exists.

### Examples
**Example 1**

- Input: `coins = [1,2,5], amount = 11`
- Output: `3`

**Example 2**

- Input: `coins = [2], amount = 3`
- Output: `-1`

**Example 3**

- Input: `coins = [1], amount = 0`
- Output: `0`

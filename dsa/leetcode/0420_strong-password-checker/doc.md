# Strong Password Checker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 420 |
| Difficulty | Hard |
| Topics | String, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/strong-password-checker/) |

## Problem Description
### Goal
Given a password string, one edit may insert one character, delete one character, or replace one character. A strong password has length from `6` through `20`, contains at least one lowercase letter, one uppercase letter, and one digit, and has no three identical consecutive characters.

Return the minimum number of edits needed to satisfy all rules simultaneously. One well-chosen edit may help both a missing character class and a repeated run, while excess-length deletions can reduce later replacement needs. Other symbols may remain but do not satisfy the three required classes. The task asks only for the optimal edit count, not a repaired password.

### Function Contract
**Inputs**

- `password`: the current password string

**Return value**

- Return the minimum number of single-character edits required to satisfy every strength rule.

### Examples
**Example 1**

- Input: `password = "a"`
- Output: `5`

**Example 2**

- Input: `password = "aA1"`
- Output: `3`

**Example 3**

- Input: `password = "1337C0d3"`
- Output: `0`

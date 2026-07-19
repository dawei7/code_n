# 2 Keys Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 650 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/2-keys-keyboard/) |

## Problem Description
### Goal
A notepad initially displays exactly one character `A`. In one operation, you may use `Copy All` to copy every character currently on the screen—partial copying is not allowed—or use `Paste` to append the text copied by the most recent copy operation.

Given `n`, return the minimum number of operations required to display exactly `n` copies of `A`. Extra copies are not allowed in the final state, and pasting before any useful copy cannot create new text. When `n` is `1`, the initial screen already meets the target and the answer is `0`.

### Function Contract
**Inputs**

- `n`: the positive target number of `A` characters

**Return value**

- The minimum number of copy and paste operations needed to display exactly `n` characters

### Examples
**Example 1**

- Input: `n = 3`
- Output: `3`

**Example 2**

- Input: `n = 1`
- Output: `0`

**Example 3**

- Input: `n = 12`
- Output: `7`

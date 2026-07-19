# 4 Keys Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 651 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/4-keys-keyboard/) |

## Problem Description
### Goal
Begin with an empty screen and a keyboard containing four keys: `A`, which writes one character; `Ctrl-A`, which selects the entire screen; `Ctrl-C`, which copies the selection; and `Ctrl-V`, which appends the most recently copied text.

Given at most `n` key presses, return the maximum number of `A` characters that can be displayed. Each key press costs one action, selecting or copying does not itself add characters, and paste uses the current clipboard contents. You may stop before using all presses when no additional action can improve the result.

### Function Contract
**Inputs**

- `n`: the positive number of keypresses available

**Return value**

- The greatest number of `A` characters that can be displayed after at most `n` keypresses

### Examples
**Example 1**

- Input: `n = 3`
- Output: `3`

**Example 2**

- Input: `n = 7`
- Output: `9`

**Example 3**

- Input: `n = 9`
- Output: `16`

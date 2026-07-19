# Bulb Switcher II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 672 |
| Difficulty | Medium |
| Topics | Math, Bit Manipulation, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/bulb-switcher-ii/) |

## Problem Description
### Goal
A room contains `n` bulbs labeled `1` through `n`, all turned on initially. Four buttons flip, respectively, all bulbs; bulbs with even labels; bulbs with odd labels; or bulbs labeled $3k + 1$ for non-negative integers `k`.

You must make exactly `presses` button presses, choosing any of the four buttons on each press and allowing the same button more than once. Return the number of different final on/off statuses reachable after all presses. Different press sequences that produce the same bulb status count only once.

### Function Contract
**Inputs**

- `n`: the positive number of bulbs
- `presses`: the exact nonnegative number of button presses

**Return value**

- The number of distinct bulb configurations reachable after exactly `presses` operations

### Examples
**Example 1**

- Input: `n = 1, presses = 1`
- Output: `2`

**Example 2**

- Input: `n = 2, presses = 1`
- Output: `3`

**Example 3**

- Input: `n = 3, presses = 2`
- Output: `7`

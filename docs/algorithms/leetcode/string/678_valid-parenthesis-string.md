# Valid Parenthesis String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_219` |
| Frontend ID | 678 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Stack, Greedy |
| Official Link | [valid-parenthesis-string](https://leetcode.com/problems/valid-parenthesis-string/) |

## Problem Description & Examples
### Goal
Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `True` if `s` is valid.

The following rules define a valid string:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

### Function Contract
**Inputs**

- `s`: str

**Return value**

bool - True if valid

### Examples
**Example 1**

- Input: `s = "(*)"`
- Output: `True`

**Example 2**

- Input: `s = ')()'`
- Output: `False`

**Example 3**

- Input: `s = '*('`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

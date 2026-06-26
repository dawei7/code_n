## Problem Description & Examples
### Goal
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket.

### Function Contract
**Inputs**

- `s`: str - containing brackets only

**Return value**

bool - True if brackets are balanced

### Examples
**Example 1**

- Input: `s = "()[]{}"`
- Output: `True`

**Example 2**

- Input: `s = '{['`
- Output: `False`

**Example 3**

- Input: `s = '()'`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

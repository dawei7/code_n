# Reverse Substrings Between Each Pair of Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1190 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reverse-substrings-between-each-pair-of-parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/).

### Goal
Reverse the characters inside every matched pair of parentheses, starting from the innermost pairs, and remove all parentheses from the final string.

### Function Contract
**Inputs**

- `s`: String containing lowercase letters and balanced parentheses.

**Return value**

String after all parenthesized reversals are applied.

### Examples
**Example 1**

- Input: `s = "(abcd)"`
- Output: `"dcba"`

**Example 2**

- Input: `s = "(u(love)i)"`
- Output: `"iloveu"`

**Example 3**

- Input: `s = "(ed(et(oc))el)"`
- Output: `"leetcode"`

---

## Solution
### Approach
One direct solution uses a stack of character buffers: push a new buffer at `(`, reverse the current buffer at `)`, and append it to the previous buffer.

A more index-oriented solution precomputes matching parentheses, then walks the string with a direction value. When the walk hits a parenthesis, jump to its match and flip direction. Letters encountered during the walk form the answer.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

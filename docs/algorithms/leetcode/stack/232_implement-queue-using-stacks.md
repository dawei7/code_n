# Implement Queue using Stacks

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_48` |
| Frontend ID | 232 |
| Difficulty | Easy |
| Topics | Stack, Design, Queue |
| Official Link | [implement-queue-using-stacks](https://leetcode.com/problems/implement-queue-using-stacks/) |

## Problem Description & Examples
### Goal
Given an encoded string `s`, return its decoded string. The encoding rule is `k[encoded_string]` where the encoded_string is repeated exactly k times.

### Function Contract
**Inputs**

- `s`: str - encoded string

**Return value**

str - decoded string

### Examples
**Example 1**

- Input: `s = "3[a]2[bc]"`
- Output: `"aaabcbc"`

**Example 2**

- Input: `s = '4[cfe]3[2[3[e]]]'`
- Output: `'cfecfecfecfeeeeeeeeeeeeeeeeeee'`

**Example 3**

- Input: `s = 'bcc'`
- Output: `'bcc'`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

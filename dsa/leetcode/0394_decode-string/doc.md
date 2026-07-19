# Decode String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 394 |
| Difficulty | Medium |
| Topics | String, Stack, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-string/) |

## Problem Description
### Goal
Given a valid encoded string, each construct `k[encoded]` represents the bracketed substring repeated exactly positive integer `k` times. Encoded regions may nest, and decimal repeat counts may contain several digits; letters outside brackets appear once in their original order.

Return the fully expanded lowercase string. Inner bracketed expressions must be decoded before their enclosing repetition is applied, and neighboring literal or repeated pieces concatenate. Digits serve only as repeat counts under the grammar, brackets are balanced, and no extra separators appear in the output. Consume the complete input rather than decoding only its first top-level component.

### Function Contract
**Inputs**

- `s`: a valid encoding containing lowercase letters, positive decimal repeat counts, and balanced square brackets

**Return value**

- Return the fully expanded lowercase string.

### Examples
**Example 1**

- Input: `s = "3[a]2[bc]"`
- Output: `"aaabcbc"`

**Example 2**

- Input: `s = "3[a2[c]]"`
- Output: `"accaccacc"`

**Example 3**

- Input: `s = "2[abc]3[cd]ef"`
- Output: `"abcabccdcdcdef"`

# Reverse Prefix of Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2000 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-prefix-of-word/) |

## Problem Description

### Goal

Given a lowercase string `word` and a lowercase character `ch`, locate the first occurrence of `ch` in `word`. If it occurs at index $i$, reverse exactly the prefix from index $0$ through index $i$, including that occurrence, while leaving every character after $i$ in its original position and order.

If `ch` does not occur anywhere in `word`, no prefix is selected and the original string must be returned unchanged.

### Function Contract

**Inputs**

- `word`: a string of $N$ lowercase English letters, where $1 \le N \le 250$.
- `ch`: one lowercase English letter.

**Return value**

Return `word` with the prefix ending at the first occurrence of `ch` reversed, or return `word` unchanged when `ch` is absent.

### Examples

**Example 1**

- Input: `word = "abcdefd", ch = "d"`
- Output: `"dcbaefd"`
- Explanation: The first `d` is at index $3$, so `"abcd"` becomes `"dcba"`.

**Example 2**

- Input: `word = "xyxzxe", ch = "z"`
- Output: `"zxyxxe"`
- Explanation: The first `z` ends the prefix `"xyxz"`, whose reversal is `"zxyx"`.

**Example 3**

- Input: `word = "abcd", ch = "z"`
- Output: `"abcd"`
- Explanation: Since `z` is absent, the string is unchanged.

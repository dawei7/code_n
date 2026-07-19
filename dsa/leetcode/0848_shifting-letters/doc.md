# Shifting Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 848 |
| Difficulty | Medium |
| Topics | Array, String, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/shifting-letters/) |

## Problem Description
### Goal
A shift replaces a lowercase English letter with the next letter of the alphabet, with `z` wrapping around to `a`. Repeating that operation advances the letter cyclically; for example, one shift changes `a` to `b`, while 26 shifts return any letter to itself.

You are given a lowercase string `s` and an equally long integer array `shifts`. For every index `i`, apply `shifts[i]` shifts to the first `i + 1` characters of the string. Return the final string after all prefix operations have been applied.

### Function Contract
**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \leq n \leq 10^5$.
- `shifts`: an integer array of length $n$, where $0 \leq \texttt{shifts[i]} \leq 10^9$.

**Return value**

Return the lowercase string produced by applying each indexed shift count to its corresponding prefix.

### Examples
**Example 1**

- Input: `s = "abc", shifts = [3,5,9]`
- Output: `"rpl"`

The successive prefix results are `"dbc"`, `"igc"`, and `"rpl"`.

**Example 2**

- Input: `s = "aaa", shifts = [1,2,3]`
- Output: `"gfd"`

**Example 3**

- Input: `s = "z", shifts = [1]`
- Output: `"a"`

The alphabet wraps after `z`.

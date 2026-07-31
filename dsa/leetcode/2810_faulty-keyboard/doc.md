# Faulty Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2810 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/faulty-keyboard/) |

## Problem Description

### Goal

A faulty keyboard behaves normally for every lowercase English letter except `i`. Whenever `i` is typed, that character does not appear on the screen; instead, the entire text already displayed is reversed. You type the characters of the given string `s` from left to right, applying this behavior after each keystroke.

Return the final text shown after all characters have been processed. Consecutive `i` characters cause consecutive reversals, so two of them restore the prior orientation. The first input character is guaranteed not to be `i`, although later characters may contain any number of triggers.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert\texttt{s}\rvert \leq 100$ and `s[0] != "i"`.

**Return value**

Return the screen text after ordinary characters have been inserted and every `i` trigger has reversed the text accumulated before it.

### Examples

**Example 1**

- Input: `s = "string"`
- Output: `"rtsng"`
- Explanation: Typing `str` produces `"str"`; the next `i` reverses it to `"rts"`, and `ng` is appended normally.

**Example 2**

- Input: `s = "poiinter"`
- Output: `"ponter"`
- Explanation: The two consecutive triggers reverse `"po"` twice, restoring it before the remaining letters are typed.

**Example 3**

- Input: `s = "abc"`
- Output: `"abc"`
- Explanation: With no trigger character, every letter is appended normally.

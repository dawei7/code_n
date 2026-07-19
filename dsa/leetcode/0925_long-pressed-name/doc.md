# Long Pressed Name

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 925 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/long-pressed-name/) |

## Problem Description

### Goal

Your friend intends to enter the string `name` on a keyboard. While a character is being typed, its key may be long pressed, causing that character to appear one or more times instead of exactly once.

Given the observed string `typed`, determine whether it could have been produced from `name` by long pressing some characters, possibly none. Every character of `name` must still appear in order, and any additional characters in `typed` must be repetitions caused by the immediately preceding intended key press.

### Function Contract

**Inputs**

- `name`: the intended name, containing only lowercase English letters and having length $m$, where $1 \le m \le 1000$.
- `typed`: the observed keyboard output, containing only lowercase English letters and having length $t$, where $1 \le t \le 1000$.

**Return value**

Return `true` if `typed` can represent `name` with zero or more long-pressed characters; otherwise return `false`.

### Examples

**Example 1**

- Input: `name = "alex", typed = "aaleex"`
- Output: `true`
- Explanation: The keys for `a` and `e` may each have been long pressed.

**Example 2**

- Input: `name = "saeed", typed = "ssaaedd"`
- Output: `false`
- Explanation: The two intended `e` characters are not both represented in `typed`.

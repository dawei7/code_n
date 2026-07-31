# Repeat String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2796 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/repeat-string/) |

## Problem Description

### Goal

Extend JavaScript strings with a method named `replicate`. Calling `str.replicate(times)` must produce a new string made by concatenating exactly `times` copies of the receiver `str` in their original order.

The implementation must not call the built-in `String.prototype.repeat` method. For the follow-up complexity model, treat each string concatenation as an $O(1)$ operation and achieve logarithmic time in the repetition count.

### Function Contract

**Inputs**

- `times`: The positive number of copies to place in the returned string, where $1 \le \texttt{times} \le 10^5$.

The receiver `str` is a string whose length is between $1$ and $1000$ characters.

**Return value**

Return the concatenation of `times` consecutive copies of the receiver string.

### Examples

**Example 1**

- Input: `str = "hello"`, `times = 2`
- Output: `"hellohello"`
- Explanation: Two copies of `"hello"` are joined.

**Example 2**

- Input: `str = "code"`, `times = 3`
- Output: `"codecodecode"`
- Explanation: The result contains three consecutive copies of `"code"`.

**Example 3**

- Input: `str = "js"`, `times = 1`
- Output: `"js"`
- Explanation: Repeating once leaves the string content unchanged.

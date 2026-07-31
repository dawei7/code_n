# Append Characters to String to Make Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2486 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/) |

## Problem Description

### Goal

Given two nonempty strings `s` and `t` made only of lowercase English letters, append characters exclusively to the end of `s` until `t` is a subsequence of the resulting string. A subsequence keeps its selected characters in their original order but may omit any number of intervening characters.

Return the minimum number of appended characters required. Existing characters of `s` cannot be reordered or removed, and every new character is placed after the entire original string, so the answer depends on how long a prefix of `t` can already be matched inside `s`.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string.
- `t`: A nonempty lowercase English string that must become a subsequence.

Let $n = \lvert\texttt{s}\rvert$ and $m = \lvert\texttt{t}\rvert$. The constraints satisfy $1 \le n,m \le 10^5$.

**Return value**

Return the minimum number of lowercase letters that must be appended to the end of `s` so that all characters of `t` can be selected in order from the extended string.

### Examples

**Example 1**

- Input: `s = "coaching", t = "coding"`
- Output: `4`
- Explanation: The prefix `"co"` already matches in `s`; appending `"ding"` completes `t`.

**Example 2**

- Input: `s = "abcde", t = "a"`
- Output: `0`
- Explanation: The target is already a subsequence of `s`.

**Example 3**

- Input: `s = "z", t = "abcde"`
- Output: `5`
- Explanation: No nonempty prefix of `t` matches, so all five target characters must be appended.

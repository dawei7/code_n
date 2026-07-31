# Lexicographically Smallest String After Substring Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2734 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/) |

## Problem Description

### Goal

Given a lowercase English string, perform exactly one operation on a nonempty contiguous substring. Replace every selected letter with the letter immediately preceding it in the alphabet: `b` becomes `a`, `c` becomes `b`, and so on, while `a` wraps around to `z`.

Return the lexicographically smallest string obtainable after that single operation. The chosen substring may contain one character or the entire string, but it cannot be empty; consequently, even a string made entirely of `a` characters must be changed somewhere.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \le \lvert s \rvert \le 3\cdot10^5$.

**Return value**

Return the lexicographically smallest string obtainable by decrementing every character of exactly one nonempty substring, using alphabetic wraparound from `a` to `z`.

### Examples

**Example 1**

- Input: `s = "cbabc"`
- Output: `"baabc"`
- Explanation: Decrementing the prefix `"cb"` changes it to `"ba"`; extending through the following `a` would wrap that position to `z`.

**Example 2**

- Input: `s = "aa"`
- Output: `"az"`
- Explanation: Some character must change, and changing the last `a` delays the unavoidable `z` as far right as possible.

**Example 3**

- Input: `s = "acbbc"`
- Output: `"abaab"`
- Explanation: The first `a` is skipped and the remaining non-`a` suffix is decremented.

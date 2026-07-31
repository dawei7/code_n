# Longest Substring of One Repeating Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2213 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/) |

## Problem Description

### Goal

Begin with a 0-indexed lowercase string `s`. Two equally long query collections describe point replacements: query $i$ changes `s[queryIndices[i]]` to `queryCharacters[i]`. Updates are permanent, so every later query operates on the already modified string.

After each replacement, find the longest contiguous substring whose characters are all equal. Return these maximum run lengths in query order, including an answer when a query writes the character already present.

### Function Contract

**Inputs**

- `s`: the initial lowercase string of length $n$, where $1 \le n \le 10^5$.
- `queryCharacters`: a lowercase string containing $q$ replacement characters.
- `queryIndices`: $q$ valid zero-based indices into `s`, where $1 \le q \le 10^5$.

**Return value**

Return a length-$q$ integer array whose $i$th value is the longest equal-character run after query $i$.

### Examples

**Example 1**

- Input: `s = "babacc"`, `queryCharacters = "bcb"`, `queryIndices = [1, 3, 3]`
- Output: `[3, 3, 4]`
- Explanation: the longest runs after the updates are `bbb`, then either `bbb` or `ccc`, then `bbbb`.

**Example 2**

- Input: `s = "abyzz"`, `queryCharacters = "aa"`, `queryIndices = [2, 1]`
- Output: `[2, 3]`
- Explanation: the unchanged `zz` first remains longest, then the prefix becomes `aaa`.

**Example 3**

- Input: `s = "a"`, `queryCharacters = "bb"`, `queryIndices = [0, 0]`
- Output: `[1, 1]`
- Explanation: every version of a one-character string has maximum run length one.

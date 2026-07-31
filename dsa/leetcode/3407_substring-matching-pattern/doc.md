# Substring Matching Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3407 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/substring-matching-pattern/) |

## Problem Description

### Goal

You are given a lowercase string `s` and a pattern `p` that contains lowercase letters and exactly one `'*'` character. The star may be replaced by any sequence of zero or more characters.

Determine whether some replacement makes the complete pattern equal to a contiguous substring of `s`. The matching substring may begin or end anywhere in `s`; the pattern does not need to cover the whole input string.

### Function Contract

**Inputs**

- `s`: The lowercase text in which a matching substring is sought.
- `p`: The lowercase pattern containing exactly one `'*'` wildcard.

Let $n=\lvert s\rvert$ and $m=\lvert p\rvert$. The constraints are $1\le n,m\le50$.

**Return value**

- `true` if the star can be replaced so that `p` matches a substring of `s`; otherwise, `false`.

### Examples

**Example 1**

- Input: `s = "leetcode", p = "ee*e"`
- Output: `true`

Replacing `'*'` with `"tcod"` makes the pattern `"eetcode"`, which occurs in `s`.

**Example 2**

- Input: `s = "car", p = "c*v"`
- Output: `false`

No substring begins with `"c"` and later ends with `"v"`.

**Example 3**

- Input: `s = "luck", p = "u*"`
- Output: `true`

The star may represent the empty string, `"c"`, or `"ck"`, so several substrings beginning with `"u"` match.

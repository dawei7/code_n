# Replace the Substring for Balanced String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1234 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) |

## Problem Description

### Goal

You are given a string `s` of length $n$ containing only the four characters `"Q"`, `"W"`, `"E"`, and `"R"`. The length is a multiple of four. The string is balanced when each of those four characters appears exactly $n/4$ times.

Choose one contiguous substring and replace it with any other string having the same length. Return the minimum possible length of a replacement that can make the entire string balanced. The replacement may contain any of the four permitted characters; if `s` is already balanced, return `0` without replacing anything.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $4\le n\le10^5$, $n$ is divisible by $4$, and every character belongs to `"QWER"`.

**Return value**

- The minimum length of a substring that can be replaced to make every character occur exactly $n/4$ times.

### Examples

**Example 1**

- Input: `s = "QWER"`
- Output: `0`

Every character already appears once.

**Example 2**

- Input: `s = "QQWE"`
- Output: `1`

Replacing one `"Q"` with `"R"` balances the string.

**Example 3**

- Input: `s = "QQQW"`
- Output: `2`

The first `"QQ"` can be replaced by `"ER"`.

# Word Pattern II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 291 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-pattern-ii/) |

## Problem Description
### Goal
Given a symbolic `pattern` and a target string `s`, assign each distinct pattern character a nonempty substring. Replacing pattern characters from left to right with their assigned strings must concatenate to exactly `s`, consuming every target character in order.

Return `True` when such an assignment exists. The mapping must be consistent and bijective: repeated pattern characters reuse the identical substring, while different characters cannot receive the same substring. Substrings may have different lengths and may repeat internally, but none may be empty. Return `False` when every possible boundary assignment leaves unmatched text or violates either mapping direction.

### Function Contract
**Inputs**

- `pattern`: the sequence of symbolic characters to replace
- `s`: the complete target string

**Return value**

`True` when a bijective substitution reconstructs `s`; otherwise `False`.

### Examples
**Example 1**

- Input: `pattern = "abab", s = "redblueredblue"`
- Output: `true`

**Example 2**

- Input: `pattern = "aaaa", s = "asdasdasdasd"`
- Output: `true`

**Example 3**

- Input: `pattern = "aabb", s = "xyzabcxzyabc"`
- Output: `false`

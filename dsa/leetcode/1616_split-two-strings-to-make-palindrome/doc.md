# Split Two Strings to Make Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1616 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-two-strings-to-make-palindrome/) |

## Problem Description
### Goal
Two lowercase strings `a` and `b` have the same length. Choose one split index and divide both strings at that same position into a prefix and a suffix. The split may occur before the first character or after the last, so either piece is allowed to be empty.

Determine whether some shared split makes either `a_prefix + b_suffix` or `b_prefix + a_suffix` a palindrome. The prefix and suffix used in one candidate must come from different input strings, and their boundary must be the same index in both strings. Return whether at least one of the two possible source directions can succeed.

### Function Contract
**Inputs**

- `a`: a lowercase English string of length $n$.
- `b`: another lowercase English string of the same length $n$, where $1 \le n \le 10^5$.

**Return value**

Return `true` if a common split index forms a palindrome in either cross-string direction; otherwise return `false`.

### Examples
**Example 1**

- Input: `a = "x", b = "y"`
- Output: `true`

**Example 2**

- Input: `a = "xbdef", b = "xecab"`
- Output: `false`

**Example 3**

- Input: `a = "ulacfd", b = "jizalu"`
- Output: `true`

# Break a Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1328 |
| Difficulty | Medium |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/break-a-palindrome/) |

## Problem Description
### Goal
Given a palindromic string `palindrome` of lowercase English letters, replace exactly one character with another lowercase letter so the resulting string is not a palindrome.

Among all valid results, return the lexicographically smallest. For equal-length strings, lexicographic order is determined by the first position where they differ. If no one-character replacement can break the palindrome, return the empty string.

The replacement character may be any lowercase English letter, but it must differ from the character it replaces because the operation is an actual change.

### Function Contract
**Inputs**

- `palindrome`: a lowercase palindromic string of length $n$, where $1\le n\le1000$.

**Return value**

The lexicographically smallest non-palindrome obtainable by replacing exactly one character, or `""` if no such string exists.

### Examples
**Example 1**

- Input: `palindrome = "abccba"`
- Output: `"aaccba"`
- Explanation: Replacing the first non-`a` in the left half yields the smallest possible differing prefix.

**Example 2**

- Input: `palindrome = "a"`
- Output: `""`
- Explanation: Every one-character string is a palindrome after any replacement.

**Example 3**

- Input: `palindrome = "aa"`
- Output: `"ab"`
- Explanation: No left-half character can be reduced, so increasing the final character minimally is optimal.

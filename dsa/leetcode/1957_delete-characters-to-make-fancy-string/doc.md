# Delete Characters to Make Fancy String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1957 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-characters-to-make-fancy-string/) |

## Problem Description
### Goal
A string is fancy when it contains no three equal consecutive characters.
Given a lowercase English string `s`, delete as few characters as possible so
that the remaining characters form a fancy string.

Deletions preserve the relative order of every retained character. Return the
final string after performing the minimum number of deletions. The contract
guarantees that this minimum-deletion result is unique.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $N$, where
  $1\le N\le10^5$.

**Return value**

- The unique fancy string obtained by deleting the minimum possible number of
  characters from `s`.

### Examples
**Example 1**

- Input: `s = "leeetcode"`
- Output: `"leetcode"`

**Example 2**

- Input: `s = "aaabaaaa"`
- Output: `"aabaa"`

**Example 3**

- Input: `s = "aab"`
- Output: `"aab"`

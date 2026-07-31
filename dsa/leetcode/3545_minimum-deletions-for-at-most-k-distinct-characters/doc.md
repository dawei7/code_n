# Minimum Deletions for At Most K Distinct Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3545 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/) |

## Problem Description

### Goal

Given a string of lowercase English letters, delete any number of individual characters so that the resulting string contains at most `k` distinct characters. The relative order of characters that remain is irrelevant to the distinct-character count.

Return the smallest possible number of deletions. If the original string already uses no more than `k` distinct letters, no deletion is necessary.

### Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters.
- `k`: The maximum number of distinct characters permitted after deletion.

The constraints are $1 \le \lvert s \rvert \le 16$ and $1 \le k \le 16$.

**Return value**

Return the minimum number of characters that must be deleted so the remaining string has at most `k` distinct letters.

### Examples

**Example 1**

- Input: `s = "abc", k = 2`
- Output: `1`
- Explanation: Removing the only occurrence of any one letter leaves two distinct letters.

**Example 2**

- Input: `s = "aabb", k = 2`
- Output: `0`
- Explanation: The string already has exactly two distinct letters.

**Example 3**

- Input: `s = "yyyzz", k = 1`
- Output: `2`
- Explanation: Deleting both `z` characters is cheaper than deleting the three `y` characters.

---

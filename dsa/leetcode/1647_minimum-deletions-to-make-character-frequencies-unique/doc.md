# Minimum Deletions to Make Character Frequencies Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1647 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) |

## Problem Description
### Goal
A string is good when no two distinct characters that remain in it have the same positive frequency. Given a lowercase English string `s`, delete as few characters as possible to make it good.

Deleting every occurrence of a character reduces its frequency to zero; zero-frequency characters are absent and do not conflict with one another. Return only the minimum number of deletions, not a resulting string.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.

**Return value**

Return the minimum number of character deletions needed so that all positive character frequencies are pairwise distinct.

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `0`

The frequencies 2 and 1 are already distinct.

**Example 2**

- Input: `s = "aaabbbcc"`
- Output: `2`

The frequencies 3, 3, and 2 can become 3, 2, and 1 with two deletions.

**Example 3**

- Input: `s = "ceabaacb"`
- Output: `2`

Deleting both copies of `c` leaves positive frequencies 4, 2, and 1.

# Minimum Deletions to Make String K-Special

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3085 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-deletions-to-make-string-k-special](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/) |

## Problem Description

### Goal

You are given a lowercase string `word` and a nonnegative integer `k`. For a character that occurs in the current string, its frequency is the number of positions containing that character.

The string is **k-special** when the absolute difference between the frequencies of every pair of characters present in the string is at most `k`. You may delete individual character occurrences, which can reduce a character's frequency or remove that character completely. Return the minimum number of deletions needed to make `word` k-special.

### Function Contract

**Inputs**

- `word`: A string of lowercase English letters, where $1 \le \lvert \texttt{word} \rvert \le 10^5$.
- `k`: The largest permitted frequency difference, where $0 \le k \le 10^5$.

Characters removed completely no longer participate in the pairwise frequency condition.

**Return value**

- The minimum number of character occurrences that must be deleted to make the remaining string k-special.

### Examples

**Example 1**

- Input: `word = "aabcaba", k = 0`
- Output: `3`
- Explanation: Delete two `a` characters and the only `c`, leaving two `a` and two `b` characters.

**Example 2**

- Input: `word = "dabdcbdcdcd", k = 2`
- Output: `2`
- Explanation: Removing the only `a` and one `d` leaves frequencies $2$, $3$, and $4$, whose maximum difference is $2$.

**Example 3**

- Input: `word = "aaabaaa", k = 2`
- Output: `1`
- Explanation: Delete the only `b`; the remaining string contains only `a`, with frequency $6$.

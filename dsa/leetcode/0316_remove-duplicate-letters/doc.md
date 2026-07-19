# Remove Duplicate Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 316 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) |

## Problem Description
### Goal
Given a nonempty lowercase string `s`, delete selected character occurrences to form a subsequence containing every distinct letter present in `s` exactly once. Retained characters must remain in their original relative order.

Among all subsequences satisfying that coverage, return the lexicographically smallest one. Choosing an early small letter is valid only when every required letter can still appear once afterward, and repeated occurrences cannot remain in the result. Lexicographic comparison uses normal lowercase alphabet order. The output length equals the number of distinct input letters and contains no character absent from the source.

### Function Contract
**Inputs**

- `s`: a nonempty string of lowercase English letters

**Return value**

The lexicographically smallest distinct-letter subsequence of `s`.

### Examples
**Example 1**

- Input: `s = "bcabc"`
- Output: `"abc"`

**Example 2**

- Input: `s = "cbacdcbc"`
- Output: `"acdb"`

**Example 3**

- Input: `s = "bbcaac"`
- Output: `"bac"`

# Count Substrings That Can Be Rearranged to Contain a String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3298 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) |

## Problem Description

### Goal

You are given lowercase English strings `word1` and `word2`. A contiguous substring of `word1` is valid if its characters can be rearranged into a string whose prefix is exactly `word2`. Any remaining characters may follow that prefix in any order.

Because rearrangement preserves character counts, a range qualifies precisely when it supplies at least the frequency required for every letter of `word2`. Return the total number of qualifying ranges, counting ranges at different positions separately even when their text is equal. The large source limit and restricted memory budget require a linear-time method with constant auxiliary storage.

### Function Contract

**Inputs**

- `word1`: The lowercase source string whose contiguous substrings are considered.
- `word2`: The lowercase prefix pattern whose complete character multiset must occur in a valid substring.

The length of `word1` is from 1 through $10^6$, while the length of `word2` is from 1 through $10^4$.

**Return value**

- The number of substrings of `word1` that can be rearranged to begin with `word2`.

### Examples

**Example 1**

- Input: `word1 = "bcca"`, `word2 = "abc"`
- Output: `1`
- Explanation: Only the entire source has at least one occurrence of each required letter.

**Example 2**

- Input: `word1 = "abcabc"`, `word2 = "abc"`
- Output: `10`
- Explanation: Ten positional ranges contain an `a`, a `b`, and a `c` and can therefore be rearranged to begin with `"abc"`.

**Example 3**

- Input: `word1 = "abcabc"`, `word2 = "aaabc"`
- Output: `0`
- Explanation: No range can supply three copies of `a` because the entire source has only two.

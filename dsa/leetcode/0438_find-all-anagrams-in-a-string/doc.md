# Find All Anagrams in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 438 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |

## Problem Description
### Goal
Given lowercase strings `s` and `p`, inspect every contiguous substring of `s` whose length equals `len(p)`. A window is an anagram of `p` when it contains exactly the same characters with the same multiplicities, regardless of their order.

Return the zero-based starting indices of all matching windows in any order. Overlapping matches must be included, while a matching character set with incorrect counts does not qualify. If `p` is longer than `s`, return an empty list. The function returns indices rather than the substrings themselves.

### Function Contract
**Inputs**

- `s`: the lowercase text string to search
- `p`: the lowercase pattern whose character multiset must match

**Return value**

- Return all matching start indices in increasing order; overlapping matches are included.

### Examples
**Example 1**

- Input: `s = "cbaebabacd", p = "abc"`
- Output: `[0, 6]`

**Example 2**

- Input: `s = "abab", p = "ab"`
- Output: `[0, 1, 2]`

**Example 3**

- Input: `s = "a", p = "a"`
- Output: `[0]`

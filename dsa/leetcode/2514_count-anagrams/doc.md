# Count Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2514 |
| Difficulty | Hard |
| Topics | Hash Table, Math, String, Combinatorics, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-anagrams/) |

## Problem Description

### Goal

You are given a string `s` containing one or more lowercase words separated by single spaces. An anagram of the whole string is formed by permuting the letters inside each word independently.

Word positions cannot be exchanged, and each resulting word must use exactly the letters of the word originally at that position. For example, `"acb dfe"` is an anagram of `"abc def"`, while swapping the words or changing their letter multisets is not allowed.

Return the number of distinct strings obtainable under these rules, modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English words separated by exactly one space.

The total string length is at most $10^5$; there are no leading, trailing, or repeated separator spaces.

**Return value**

The number of distinct valid anagrams of `s`, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `s = "too hot"`
- **Output:** `18`
- **Explanation:** `too` has three placements for its unique `t`, and `hot` has six letter permutations, giving $3\cdot6=18$ strings.

#### Example 2

- **Input:** `s = "aa"`
- **Output:** `1`
- **Explanation:** Exchanging the two equal letters does not create a different word.

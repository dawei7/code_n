# Count Prefix and Suffix Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3042 |
| Difficulty | Easy |
| Topics | Array, String, Trie, Rolling Hash, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/) |

## Problem Description

### Goal

You are given a 0-indexed string array `words`. Define `isPrefixAndSuffix(str1, str2)` to be true exactly when `str1` is both a prefix and a suffix of `str2`.

For example, `isPrefixAndSuffix("aba", "ababa")` is true because `"ababa"` begins and ends with `"aba"`. In contrast, `isPrefixAndSuffix("abc", "abcd")` is false because the second string does not end with the first.

Return the number of index pairs `(i, j)` for which $i<j$ and `isPrefixAndSuffix(words[i], words[j])` is true. Equal strings at different indices are allowed and satisfy both conditions.

### Function Contract

Let $n=\lvert\texttt{words}\rvert$ and let $L$ be the maximum length of any word.

**Inputs**

- `words`: An array with $1 \le n \le 50$; every entry contains only lowercase English letters and has length from `1` through `10`, so $1 \le L \le 10$.

**Return value**

Return the number of ordered index pairs `(i, j)` with $i<j$ for which `words[i]` is simultaneously a prefix and a suffix of `words[j]`.

### Examples

#### Example 1

- **Input:** `words = ["a","aba","ababa","aa"]`
- **Output:** `4`
- **Explanation:** The valid pairs are `(0,1)`, `(0,2)`, `(0,3)`, and `(1,2)`.

#### Example 2

- **Input:** `words = ["pa","papa","ma","mama"]`
- **Output:** `2`
- **Explanation:** The valid pairs are `(0,1)` and `(2,3)`.

#### Example 3

- **Input:** `words = ["abab","ab"]`
- **Output:** `0`
- **Explanation:** The earlier word is longer than the later word, so it cannot be either its prefix or its suffix.

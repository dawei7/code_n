# Count of Substrings Containing Every Vowel and K Consonants I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3305 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/) |

## Problem Description

### Goal

Given a lowercase string `word` and a non-negative integer `k`, consider every non-empty contiguous substring. A substring qualifies only when it contains each of the five vowels `a`, `e`, `i`, `o`, and `u` at least once.

It must also contain exactly `k` consonants; extra vowel occurrences are allowed and do not affect that count. Return the number of qualifying positional ranges, counting equal substring text separately when it occurs at different indices.

### Function Contract

**Inputs**

- `word`: A lowercase English string of length from 5 through 250.
- `k`: The exact required consonant count, from 0 through `word.length - 5`.

**Return value**

- The number of substrings containing all five vowels and exactly `k` consonants.

### Examples

#### Example 1

- **Input:** `word = "aeioqq"`, `k = 1`
- **Output:** `0`
- **Explanation:** No substring contains all five vowels because `u` is absent.

#### Example 2

- **Input:** `word = "aeiou"`, `k = 0`
- **Output:** `1`
- **Explanation:** The whole string contains every vowel and no consonants.

#### Example 3

- **Input:** `word = "ieaouqqieaouqq"`, `k = 1`
- **Output:** `3`
- **Explanation:** Exactly three ranges contain all vowels and one of the `q` characters.

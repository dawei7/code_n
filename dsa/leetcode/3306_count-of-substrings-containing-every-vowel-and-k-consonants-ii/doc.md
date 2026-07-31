# Count of Substrings Containing Every Vowel and K Consonants II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3306 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) |

## Problem Description

### Goal

Given a lowercase English string `word` and a nonnegative integer `k`, count its substrings that contain every vowel—`a`, `e`, `i`, `o`, and `u`—at least once and contain exactly `k` consonants. A substring is a contiguous, nonempty range of the original string, so identical text occurring at different positions represents different ranges and must be counted separately.

Additional occurrences of a required vowel are allowed, and their positions may appear in any order. The consonant condition is exact: a range with fewer or more than `k` non-vowel letters does not qualify. Return the total number of qualifying positional ranges; the result may exceed a 32-bit integer.

### Function Contract

**Inputs**

- `word`: A lowercase English string with $5\leq\lvert word\rvert\leq2\cdot10^5$.
- `k`: The exact number of consonants required, where $0\leq k\leq\lvert word\rvert-5$.

**Return value**

Return the number of substrings that contain all five vowels at least once and exactly `k` consonants.

### Examples

**Example 1**

- Input: `word = "aeioqq", k = 1`
- Output: `0`

No substring contains `u`, so none can contain every vowel.

**Example 2**

- Input: `word = "aeiou", k = 0`
- Output: `1`

The complete string is the only range containing every vowel, and it has no consonants.

**Example 3**

- Input: `word = "ieaouqqieaouqq", k = 1`
- Output: `3`

Exactly three positional ranges include all five vowels while containing one consonant.

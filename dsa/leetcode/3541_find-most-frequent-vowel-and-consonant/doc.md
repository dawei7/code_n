# Find Most Frequent Vowel and Consonant

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3541 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/) |

## Problem Description

### Goal

Given a string of lowercase English letters, determine the greatest frequency attained by any vowel and the greatest frequency attained by any consonant. The vowels are `a`, `e`, `i`, `o`, and `u`; every other lowercase English letter is a consonant.

Return the sum of those two maximum frequencies. Ties within either category do not matter because only the frequency is needed. If the string contains no letter from one category, use $0$ as that category's maximum frequency.

### Function Contract

**Inputs**

- `s`: A string consisting only of lowercase English letters.

The string length $n$ satisfies $1 \le n \le 100$.

**Return value**

Return the maximum vowel frequency plus the maximum consonant frequency, treating a missing category as having frequency $0$.

### Examples

#### Example 1

- **Input:** `s = "successes"`
- **Output:** `6`
- **Explanation:** `e` occurs twice, the most among vowels, while `s` occurs four times, the most among consonants. Their frequencies sum to $2 + 4 = 6$.

#### Example 2

- **Input:** `s = "aeiaeia"`
- **Output:** `3`
- **Explanation:** `a` is the most frequent vowel with three occurrences, and the string has no consonants.

---

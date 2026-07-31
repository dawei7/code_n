# Valid Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3136 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-word/) |

## Problem Description

### Goal

You are given a string `word`. Determine whether it satisfies every condition required of a valid word.

A valid word contains at least three characters and uses only decimal digits, uppercase English letters, or lowercase English letters. It must also contain at least one vowel and at least one consonant. The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, together with their uppercase forms; every other English letter is a consonant. Digits count toward the length but satisfy neither letter requirement.

Return `true` exactly when all four conditions hold. Otherwise, return `false`.

### Function Contract

Let $n = \lvert\texttt{word}\rvert$.

**Inputs**

- `word`: A string with $1 \le n \le 20$. Every character is an uppercase or lowercase English letter, a decimal digit, `'@'`, `'#'`, or `'$'`.

**Return value**

- Return `true` if `word` has valid length and characters and contains both a vowel and a consonant; otherwise return `false`.

### Examples

**Example 1**

- Input: `word = "234Adas"`
- Output: `true`
- Explanation: The length is sufficient, every character is alphanumeric, and the word contains vowels and consonants.

**Example 2**

- Input: `word = "b3"`
- Output: `false`
- Explanation: The word has fewer than three characters and contains no vowel.

**Example 3**

- Input: `word = "a3$e"`
- Output: `false`
- Explanation: The dollar sign is not allowed, and the word contains no consonant.

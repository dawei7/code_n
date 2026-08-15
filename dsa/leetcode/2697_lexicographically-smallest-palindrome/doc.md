# Lexicographically Smallest Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2697 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/lexicographically-smallest-palindrome/) |

## Problem Description

### Goal

Given a string `s` made only of lowercase English letters, an operation may replace any one character with another lowercase English letter.

Transform `s` into a palindrome using the minimum possible number of operations. When several palindromes require that same minimum number, choose the lexicographically smallest one: at the first position where two candidates differ, the chosen result must contain the alphabetically earlier letter.

Return the resulting palindrome. Its length and middle character, when the length is odd, remain unchanged by the transformation.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert s \rvert \leq 1000$.

**Return value**

Return the lexicographically smallest palindrome obtainable with the minimum number of single-character replacements.

### Examples

#### Example 1

- **Input:** `s = "egcfe"`
- **Output:** `"efcfe"`
- **Explanation:** One replacement is necessary; changing `'g'` to `'f'` gives the smallest result among the one-operation palindromes.

#### Example 2

- **Input:** `s = "abcd"`
- **Output:** `"abba"`
- **Explanation:** Both mirrored pairs differ, so two replacements are necessary. Choosing the smaller letter in each pair produces the smallest qualifying palindrome.

#### Example 3

- **Input:** `s = "seven"`
- **Output:** `"neven"`
- **Explanation:** Only the outer pair differs, and replacing `'s'` with `'n'` completes the palindrome in one operation.

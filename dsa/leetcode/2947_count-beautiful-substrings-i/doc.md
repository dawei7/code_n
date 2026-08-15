# Count Beautiful Substrings I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2947 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Enumeration, Number Theory, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-beautiful-substrings-i/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and a positive integer `k`.
For any string, let its vowel count include occurrences of `a`, `e`, `i`,
`o`, and `u`; every other lowercase English letter is a consonant.

A nonempty substring is beautiful when it contains equally many vowels and
consonants and the product of those two counts is divisible by `k`. Return
the number of contiguous substrings of `s` that are beautiful.

### Function Contract

**Inputs**

- `s`: the lowercase English source string
- `k`: the positive divisor applied to the count product

Let $N=\lvert\texttt{s}\rvert$. The contract guarantees
$1\le N\le1000$ and $1\le k\le1000$.

**Return value**

The number of nonempty substrings whose vowel and consonant counts are equal
and whose count product is divisible by `k`.

### Examples

#### Example 1

- **Input:** `s = "baeyh", k = 2`
- **Output:** `2`
- **Explanation:** `"baey"` and `"aeyh"` each contain two vowels and two
  consonants.

#### Example 2

- **Input:** `s = "abba", k = 1`
- **Output:** `3`
- **Explanation:** `"ab"`, `"ba"`, and `"abba"` are balanced, and every
  integer product is divisible by `1`.

#### Example 3

- **Input:** `s = "bcdf", k = 1`
- **Output:** `0`
- **Explanation:** No substring contains equal positive counts of vowels and
  consonants.

# Vowel Spellchecker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 966 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [vowel-spellchecker](https://leetcode.com/problems/vowel-spellchecker/) |

## Problem Description

### Goal

Given a `wordlist`, correct every string in `queries` by applying three matching rules in strict priority order. An exact case-sensitive match returns the query itself. Otherwise, a case-insensitive match returns the first matching word from `wordlist`. If neither applies, treat each vowel—`a`, `e`, `i`, `o`, or `u`—as interchangeable after ignoring case; a match under that rule also returns the first corresponding word from `wordlist`.

Vowel replacement does not insert or delete characters, and consonants must still agree. If a query matches under none of the three rules, its answer is the empty string. Return the corrections in the same order as the queries.

### Function Contract

**Inputs**

- `wordlist`: between $1$ and $5000$ English-letter strings.
- `queries`: between $1$ and $5000$ English-letter strings to correct.
- Every string has length from $1$ through $7$.
- Define the total number of input characters as

$$
S = \sum_{w \in \texttt{wordlist}} \lvert w \rvert + \sum_{q \in \texttt{queries}} \lvert q \rvert.
$$

**Return value**

Return one correction per query, preserving query order and the original capitalization of the chosen `wordlist` entry.

### Examples

**Example 1**

- Input: `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]`
- Output: `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]`

**Example 2**

- Input: `wordlist = ["yellow"], queries = ["YellOw"]`
- Output: `["yellow"]`

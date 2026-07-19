# Find Common Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1002 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-common-characters/) |

## Problem Description

### Goal

Given an array of lowercase strings `words`, return every character that appears in all of the strings. Character multiplicity matters: a letter occurring at least twice in every word must appear twice in the answer, while a third copy is included only if every word also contains a third copy.

The answer may be returned in any order. Each returned element is a one-character string, and the result represents the multiset intersection of the character occurrences in all input words.

### Function Contract

**Inputs**

- `words`: a list of $W$ nonempty lowercase English strings, where $1\le W\le100$ and every string has length from $1$ through $100$.

Define the total input length as

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

**Return value**

- The characters common to every word, repeated according to their minimum frequency across the words, in any order.

### Examples

**Example 1**

- Input: `words = ["bella", "label", "roller"]`
- Output: `["e", "l", "l"]`

**Example 2**

- Input: `words = ["cool", "lock", "cook"]`
- Output: `["c", "o"]`

**Example 3**

- Input: `words = ["aaa", "aa", "aaaa"]`
- Output: `["a", "a"]`
- Explanation: Every word contains at least two copies of `"a"`, but not every word contains three.

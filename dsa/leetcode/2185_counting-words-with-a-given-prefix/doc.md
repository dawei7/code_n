# Counting Words With a Given Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2185 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/counting-words-with-a-given-prefix/) |

## Problem Description

### Goal

Given an array of lowercase strings `words` and another lowercase string
`pref`, inspect every word independently. A prefix is a contiguous substring
that starts at the word's first character; it does not count when the same
characters occur only in the middle or at the end.

Count how many array entries have `pref` as a prefix. Duplicate strings occupy
separate positions and each matching occurrence contributes one to the
answer. A word shorter than `pref` cannot match it.

### Function Contract

**Inputs**

- `words`: an array containing between one and 100 lowercase strings, each
  with length in `[1,100]`.
- `pref`: a lowercase string with length in `[1,100]`.

Define

$$
C=\sum_{w\in\texttt{words}}
\min\bigl(\lvert w\rvert,\lvert\texttt{pref}\rvert\bigr).
$$

**Return value**

Return the number of entries in `words` whose leading characters equal
`pref`.

### Examples

#### Example 1

- **Input:** `words = ["pay","attention","practice","attend"]`, `pref = "at"`
- **Output:** `2`

#### Example 2

- **Input:** `words = ["leetcode","win","loops","success"]`, `pref = "code"`
- **Output:** `0`

#### Example 3

- **Input:** `words = ["a","a","ab"]`, `pref = "a"`
- **Output:** `3`

# Capitalize the Title

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2129 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/capitalize-the-title/) |

## Problem Description

### Goal

You are given a title containing one or more non-empty words. Every word uses
English letters, adjacent words are separated by exactly one space, and the
title has no leading or trailing spaces.

Normalize each word according to its length. Words containing one or two
letters must be entirely lowercase. For every longer word, make its first
letter uppercase and all of its remaining letters lowercase. Return the title
with the original word order and single-space separators preserved.

### Function Contract

**Inputs**

- `title`: A string of length from $1$ through $100$, containing non-empty
  English-letter words separated by single spaces.

**Return value**

The title after applying the required capitalization rule independently to
every word.

### Examples

#### Example 1

- **Input:** `title = "capiTalIze tHe titLe"`
- **Output:** `"Capitalize The Title"`

#### Example 2

- **Input:** `title = "First leTTeR of EACH Word"`
- **Output:** `"First Letter of Each Word"`
- **Explanation:** The two-letter word `"of"` becomes lowercase; every longer
  word receives an uppercase initial letter and a lowercase remainder.

#### Example 3

- **Input:** `title = "i lOve leetcode"`
- **Output:** `"i Love Leetcode"`
- **Explanation:** The one-letter word `"i"` remains lowercase.

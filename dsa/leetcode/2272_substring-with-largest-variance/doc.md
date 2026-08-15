# Substring With Largest Variance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2272 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/substring-with-largest-variance/) |

## Problem Description

### Goal

For any nonempty string, choose two characters that are both present in that
string and subtract one occurrence count from the other. The string's variance
is the largest difference obtainable from such a choice. The two selected
characters are allowed to be the same, which guarantees variance zero when no
positive difference is possible.

Given a lowercase English string `s`, consider every contiguous nonempty
substring. Return the largest variance achieved by any of them. A qualifying
positive difference must involve both selected distinct characters inside the
same substring; a run containing only one character does not create variance
against an absent character.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1\le n\le10^4$.

**Return value**

Return the maximum, over every substring and every ordered pair of characters
present in that substring, of the first character's count minus the second
character's count.

### Examples

#### Example 1

- **Input:** `s = "aababbb"`
- **Output:** `3`

The substring `"babbb"` contains four `b` characters and one `a`, producing
variance $4-1=3$.

#### Example 2

- **Input:** `s = "abcde"`
- **Output:** `0`

Every character occurs once, so no substring has unequal positive counts for
two characters that it contains.

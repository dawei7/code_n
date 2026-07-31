# Number of Ways to Build House of Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2189 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/) |

## Problem Description

### Goal

A house of cards has one or more rows. Each triangle uses two leaning cards,
and every adjacent pair of triangles in the same row has one horizontal card
between them. A triangle above the first row must rest on one of the horizontal
cards in the row immediately below it.

Within every higher row, triangles occupy the available supporting positions
from left to right without gaps. Using all `n` available cards, count the
distinct valid houses. Two houses are different when some corresponding row
contains a different number of cards.

### Function Contract

**Inputs**

- `n`: the total number of available cards, with $1\le n\le500$.

**Return value**

Return the number of distinct valid houses that use exactly all $n$ cards.

### Examples

**Example 1**

- Input: `n = 16`
- Output: `2`

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 4`
- Output: `0`

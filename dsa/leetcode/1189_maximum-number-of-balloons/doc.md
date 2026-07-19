# Maximum Number of Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1189 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/) |

## Problem Description

### Goal

You are given a string `text` containing lowercase English letters. Its characters are the available supply for spelling the word `"balloon"`; each occurrence in `text` may be used at most once.

Determine the maximum number of complete instances of `"balloon"` that can be formed. Letters not used by that word may be ignored, while repeated letters must be supplied separately for every copy.

### Function Contract

**Inputs**

- `text`: A string of length $n$, where $1\le n\le10^4$, containing only lowercase English letters.

**Return value**

- The greatest number of complete `"balloon"` words that can be assembled from the characters of `text` without reusing a character.

### Examples

**Example 1**

- Input: `text = "nlaebolko"`
- Output: `1`

The available letters contain one complete set for `"balloon"`.

**Example 2**

- Input: `text = "loonbalxballpoon"`
- Output: `2`

**Example 3**

- Input: `text = "leetcode"`
- Output: `0`

The required letters cannot all be supplied even once.

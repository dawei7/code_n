# Unique Substrings in Wraparound String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 467 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) |

## Problem Description
### Goal
The infinite wraparound string repeats the lowercase alphabet forever, so adjacent characters advance by one with `z` followed by `a`. Given a lowercase string `p`, consider all of its nonempty contiguous substrings.

Return how many unique nonempty substring texts also occur in that infinite cyclic sequence. Repeated occurrences of the same text in `p` count once, while different lengths or ending characters define different candidates. A valid substring must follow the cyclic successor rule at every adjacent position; it cannot skip characters. The function returns the unique count rather than the substrings themselves.

### Function Contract
**Inputs**

- `p`: a string of lowercase English letters

**Return value**

- The number of distinct substrings whose adjacent letters advance by one cyclically, including `z` followed by `a`

### Examples
**Example 1**

- Input: `p = "a"`
- Output: `1`

**Example 2**

- Input: `p = "cac"`
- Output: `2`

**Example 3**

- Input: `p = "zab"`
- Output: `6`

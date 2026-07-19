# Maximum Score After Splitting a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1422 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) |

## Problem Description

### Goal

Split the binary string `s` into two nonempty contiguous parts. The score of a split is the number of `0` characters in its left part plus the number of `1` characters in its right part.

Evaluate every legal boundary between adjacent characters and return the maximum score. Neither part may be empty, so the split must occur after the first character and before the last character.

### Function Contract

**Inputs**

- `s`: a binary string of length $n$, where $2 \le n \le 500$.

**Return value**

- The greatest possible value of left-side zeros plus right-side ones over all nonempty two-part splits.

### Examples

**Example 1**

- Input: `s = "011101"`
- Output: `5`

**Example 2**

- Input: `s = "00111"`
- Output: `5`

**Example 3**

- Input: `s = "1111"`
- Output: `3`

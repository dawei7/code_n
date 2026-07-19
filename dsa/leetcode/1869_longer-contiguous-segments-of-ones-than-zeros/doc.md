# Longer Contiguous Segments of Ones than Zeros

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) |
| Frontend ID | 1869 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a nonempty binary string `s`, divide it conceptually into maximal contiguous segments of equal digits. A segment of ones consists only of consecutive `"1"` characters, and a segment of zeros consists only of consecutive `"0"` characters. Only uninterrupted lengths matter; separate segments of the same digit are not combined.

Return `true` exactly when the longest segment of ones is strictly longer than the longest segment of zeros. Equal maximum lengths must return `false`. If one digit does not occur, its longest segment is defined to have length zero, so an all-ones string succeeds while an all-zeros string does not.

### Function Contract

**Inputs**

- `s`: a binary string with $1 \le \lvert s\rvert \le 100$.
- Let $N = \lvert s\rvert$.

**Return value**

- Return `true` when the maximum length of a contiguous `"1"` segment is strictly greater than the maximum length of a contiguous `"0"` segment.
- Otherwise, including when the two maxima are equal, return `false`.

### Examples

**Example 1**

- Input: `s = "1101"`
- Output: `true`

The longest ones segment has length two, while the longest zeros segment has length one.

**Example 2**

- Input: `s = "111000"`
- Output: `false`

Both longest segments have length three, and equality is not sufficient.

**Example 3**

- Input: `s = "110100010"`
- Output: `false`

The longest ones segment has length two, but the longest zeros segment has length three.

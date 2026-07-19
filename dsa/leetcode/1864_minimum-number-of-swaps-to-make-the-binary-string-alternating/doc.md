# Minimum Number of Swaps to Make the Binary String Alternating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1864 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) |

## Problem Description
### Goal
You are given a binary string `s`. A string is alternating when every pair of
adjacent characters differs, as in `"010"` or `"1010"`. In one operation, you
may swap any two characters in the string; the chosen positions do not need to
be adjacent.

Return the minimum number of such swaps required to make `s` alternating. If
the available counts of zeros and ones cannot form any alternating string,
return `-1`.

### Function Contract
**Inputs**

- `s`: a binary string of length $n$, where $1 \le n \le 1000$ and every
  character is either `"0"` or `"1"`.

**Return value**

The minimum number of arbitrary-position swaps needed to produce an
alternating string, or `-1` when no alternating arrangement exists.

### Examples
**Example 1**

- Input: `s = "111000"`
- Output: `1`

**Example 2**

- Input: `s = "010"`
- Output: `0`

**Example 3**

- Input: `s = "1110"`
- Output: `-1`

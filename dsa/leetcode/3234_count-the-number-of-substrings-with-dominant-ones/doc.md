# Count the Number of Substrings With Dominant Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3234 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/) |

## Problem Description

### Goal

You are given a binary string `s`. A substring has dominant ones when its number of `1` characters is at least the square of its number of `0` characters. The zero count is squared before comparison, while the one count enters linearly, and equality qualifies.

Count every nonempty contiguous substring satisfying this condition. Substrings with different endpoint positions count separately even when their text is identical.

### Function Contract

**Inputs**

- `s`: A binary string with $1 \leq \lvert\texttt{s}\rvert \leq 4\cdot10^4$.

Let $n=\lvert\texttt{s}\rvert$.

**Return value**

Return the number of substrings for which $#1\geq(\#0)^2$.

### Examples

#### Example 1

- **Input:** `s = "00011"`
- **Output:** `5`
- **Explanation:** The dominant substrings are the two single `1` characters, `"01"`, `"11"`, and `"011"`.

#### Example 2

- **Input:** `s = "101101"`
- **Output:** `16`
- **Explanation:** Of the $21$ total substrings, exactly five fail the dominance inequality.

#### Example 3

- **Input:** `s = "1111"`
- **Output:** `10`
- **Explanation:** Every substring contains zero zeroes, so all $4\cdot5/2$ substrings qualify.

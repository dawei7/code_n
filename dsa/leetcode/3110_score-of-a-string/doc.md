# Score of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3110 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [score-of-a-string](https://leetcode.com/problems/score-of-a-string/) |

## Problem Description

### Goal

You are given a string `s`. Its score measures how far each character is from the character immediately following it in the ASCII table. For every adjacent pair, take the absolute difference between the two ASCII values, so the direction of the change does not affect that pair's contribution.

Return the sum of those contributions across the whole string. Each neighboring pair is included exactly once. The string contains only lowercase English letters and always has at least two characters, so there is at least one adjacent pair to score.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with $2 \le \lvert\texttt{s}\rvert \le 100$.

**Return value**

- The sum of the absolute ASCII-value differences for all adjacent characters in `s`.

### Examples

#### Example 1

- **Input:** `s = "hello"`
- **Output:** `13`
- **Explanation:** The four contributions are $3$, $7$, $0$, and $3$.

#### Example 2

- **Input:** `s = "zaz"`
- **Output:** `50`
- **Explanation:** Both adjacent pairs differ by $25$ in ASCII value.

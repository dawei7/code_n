# Find the Longest Balanced Substring of a Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2609 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/) |

## Problem Description

### Goal

You are given a binary string `s`. A substring is balanced when it consists of some zeroes followed by the same number of ones. Every zero in that substring must therefore occur before every one; arrangements that switch back to zero after a one are not balanced.

Find the greatest length among all balanced substrings of `s`. A substring must occupy consecutive positions in the original string. The empty substring also qualifies, so the result is zero when no nonempty balanced substring exists.

### Function Contract

**Inputs**

- `s`: A string containing only `0` and `1`, with $1 \leq \lvert s \rvert \leq 50$.

**Return value**

Return the length of the longest balanced substring.

### Examples

**Example 1**

- Input: `s = "01000111"`
- Output: `6`
- Explanation: `"000111"` is balanced and has length six.

**Example 2**

- Input: `s = "00111"`
- Output: `4`
- Explanation: `"0011"` is the longest balanced choice.

**Example 3**

- Input: `s = "111"`
- Output: `0`
- Explanation: No nonempty substring contains a zero-run followed by an equally long one-run.

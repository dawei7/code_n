# Maximum Length Substring With Two Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3090 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) |

## Problem Description

### Goal

Given a string `s`, consider its contiguous substrings. A substring is valid when every character appearing inside it occurs at most two times. It may begin and end at any positions, but it must preserve the original order and adjacency of the selected characters.

Return the maximum length among all valid substrings. The chosen substring may contain many different lowercase letters; the restriction applies independently to the frequency of each letter, rather than to the total number of distinct letters.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters, with $2 \leq \lvert s \rvert \leq 100$.

Let $n = \lvert s \rvert$.

**Return value**

Return an integer equal to the greatest length of a contiguous substring in which no character occurs more than twice.

### Examples

**Example 1**

- Input: `s = "bcbbbcba"`
- Output: `4`
- Explanation: `"bcba"` is a length-four substring whose characters each occur at most twice. No longer substring satisfies the limit.

**Example 2**

- Input: `s = "aaaa"`
- Output: `2`
- Explanation: Any two adjacent letters are valid, while every substring of length three contains `'a'` three times.

**Example 3**

- Input: `s = "abcdef"`
- Output: `6`
- Explanation: Every character is distinct, so the entire string is valid.

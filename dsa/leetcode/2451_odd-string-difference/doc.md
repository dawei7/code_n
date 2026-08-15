# Odd String Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2451 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Odd String Difference](https://leetcode.com/problems/odd-string-difference/) |

## Problem Description

### Goal

You are given an array `words` whose lowercase strings all have the same length. Convert a word into a difference array by subtracting the alphabet position of each character from that of the following character. For example, `"acb"` produces `[2, -1]` because the letters have positions 0, 2, and 1.

Every word except one has the same difference array. Return the unique word whose adjacent-letter differences do not match that shared pattern.

### Function Contract

**Inputs**

- `words`: A list of $p$ equal-length lowercase English strings, where $3 \le p \le 100$.

Let $m$ be the common word length. The constraints guarantee $2 \le m \le 20$ and exactly one word has a different difference array.

**Return value**

- The word whose length-$(m-1)$ adjacent-difference array is unique.

### Examples

#### Example 1

- **Input:** `words = ["adc", "wzy", "abc"]`
- **Output:** `"abc"`
- **Explanation:** The first two words produce `[3, -1]`, while `"abc"` produces `[1, 1]`.

#### Example 2

- **Input:** `words = ["aaa", "bob", "ccc", "ddd"]`
- **Output:** `"bob"`
- **Explanation:** Every constant-letter word produces `[0, 0]`; `"bob"` produces `[13, -13]`.

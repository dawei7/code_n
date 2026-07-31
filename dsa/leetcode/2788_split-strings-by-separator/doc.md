# Split Strings by Separator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2788 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-strings-by-separator/) |

## Problem Description

### Goal

Given an array of strings `words` and a single character `separator`, split every word wherever that separator occurs. A word may contain the separator more than once, so processing one word can produce any number of pieces rather than only two.

Combine the pieces from all words into one list in their original left-to-right order. The separator itself does not appear in a piece, and every empty piece created by a leading, trailing, or adjacent separator must be omitted.

### Function Contract

**Inputs**

- `words`: An array of strings, where $1 \le \lvert\texttt{words}\rvert \le 100$ and $1 \le \lvert\texttt{words[i]}\rvert \le 20$. Each string contains lowercase English letters or characters from `".,|$#@"`.
- `separator`: One character from `".,|$#@"` used as the delimiter.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

denote the total number of input characters.

**Return value**

Return all non-empty pieces in encounter order after splitting each word by `separator`.

### Examples

**Example 1**

- Input: `words = ["one.two.three", "four.five", "six"], separator = "."`
- Output: `["one", "two", "three", "four", "five", "six"]`
- Explanation: Periods divide the first two words, while the final word remains whole.

**Example 2**

- Input: `words = ["$easy$", "$problem$"], separator = "$"`
- Output: `["easy", "problem"]`
- Explanation: The pieces outside the letters are empty and therefore excluded.

**Example 3**

- Input: `words = ["|||"], separator = "|"`
- Output: `[]`
- Explanation: Splitting produces only empty pieces, so the result contains nothing.

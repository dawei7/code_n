# Check if a String Is an Acronym of Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2828 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/) |

## Problem Description
### Goal

You are given an array of strings `words` and a string `s`. Form the acronym of `words` by taking the first character from every word and concatenating those characters in the same order as the array.

Determine whether the resulting acronym is exactly `s`. Every word contributes one character, so a candidate with a different length cannot be the acronym even if all compared positions match.

Return `True` when `s` is the acronym of `words`; otherwise, return `False`.

### Function Contract
**Inputs**

- `words`: A list of $n$ nonempty strings, where $1 \le n \le 100$. Each word has between $1$ and $10$ lowercase English letters.
- `s`: A string of $m$ lowercase English letters, where $1 \le m \le 100$.

**Return value**

Return whether `s` equals the ordered concatenation of the first character of every string in `words`.

### Examples
**Example 1**

- Input: `words = ["alice", "bob", "charlie"], s = "abc"`
- Output: `True`
- Explanation: The first characters are `a`, `b`, and `c`, which form `"abc"`.

**Example 2**

- Input: `words = ["an", "apple"], s = "a"`
- Output: `False`
- Explanation: Both words contribute a character, so the generated acronym is `"aa"`, not `"a"`.

**Example 3**

- Input: `words = ["never", "gonna", "give", "up", "on", "you"], s = "ngguoy"`
- Output: `True`
- Explanation: Reading the first characters in order produces `"ngguoy"`.

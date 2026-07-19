# Maximum Length of a Concatenated String with Unique Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1239 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) |

## Problem Description

### Goal

You are given an array `arr` of lowercase English strings. Select a subsequence of these strings and concatenate the selected strings without changing their original order. The resulting string is valid only when every character in the entire concatenation is unique.

Return the maximum possible length of a valid concatenation. You may delete any number of array elements, including all of them, so the empty concatenation of length zero is always available. A source string that already repeats one of its own characters cannot participate in any valid result.

### Function Contract

**Inputs**

- `arr`: A list of $n$ lowercase strings, where $1\le n\le16$ and each string has length from $1$ through $26$.

Define the total number of input characters as

$$
S = \sum_{w\in\texttt{arr}} \lvert w\rvert.
$$

**Return value**

- The maximum length of a concatenation formed from a subsequence of `arr` whose characters are all unique.

### Examples

**Example 1**

- Input: `arr = ["un","iq","ue"]`
- Output: `4`

Either `"uniq"` or `"ique"` has four distinct characters.

**Example 2**

- Input: `arr = ["cha","r","act","ers"]`
- Output: `6`

Valid longest choices include `"chaers"` and `"acters"`.

**Example 3**

- Input: `arr = ["abcdefghijklmnopqrstuvwxyz"]`
- Output: `26`

The only source string already contains every lowercase letter exactly once.

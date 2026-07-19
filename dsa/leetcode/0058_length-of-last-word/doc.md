# Length of Last Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 58 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-last-word/) |

## Problem Description
### Goal
You are given a nonempty string containing letters and spaces, with at least one word. A word is a maximal substring consisting only of non-space characters; one or more spaces separate neighboring words.

Return the number of letters in the final word. Any spaces after that word are ignored, as are all earlier words and their separators. A string containing only one word returns that word's full length, whether or not spaces surround it.

### Function Contract
**Inputs**

- `s`: a nonempty string containing at least one word

**Return value**

The integer length of the last word.

### Examples
**Example 1**

- Input: `s = "Hello World"`
- Output: `5`

**Example 2**

- Input: `s = "   fly me   to   the moon  "`
- Output: `4`

**Example 3**

- Input: `s = "a"`
- Output: `1`

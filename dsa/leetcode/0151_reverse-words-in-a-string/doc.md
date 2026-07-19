# Reverse Words in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 151 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/) |

## Problem Description
### Goal
Given a string containing at least one word and space characters, treat each maximal sequence of non-space characters as one word. Reverse the order of the words so the last original word appears first and the first original word appears last.

Return the reordered words joined by exactly one space. Discard all original leading and trailing spaces, and collapse every internal run of multiple spaces instead of preserving its width. Characters inside each word must remain in their original order; only whole-word positions are reversed. The result must contain no space at either end.

### Function Contract
**Inputs**

- `s`: a string containing words separated by one or more space characters

**Return value**

The words in reverse order, joined by exactly one space with no space at either end.

### Examples
**Example 1**

- Input: `s = "the sky is blue"`
- Output: `"blue is sky the"`

**Example 2**

- Input: `s = "  hello world  "`
- Output: `"world hello"`

**Example 3**

- Input: `s = "a good   example"`
- Output: `"example good a"`

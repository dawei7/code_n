# Number of Segments in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 434 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-segments-in-a-string/) |

## Problem Description
### Goal
Given a string `s`, a segment is a maximal contiguous run of characters that does not contain the space character. One or more spaces separate neighboring segments, while leading and trailing spaces do not create empty segments.

Return the total number of segments. Punctuation and other non-space characters remain part of their surrounding segment rather than acting as separators. An empty string or a string containing only spaces returns `0`, and a run containing one character counts as one segment. The task returns only the count, not the extracted text pieces.

### Function Contract
**Inputs**

- `s`: a string whose segments are separated by one or more space characters

**Return value**

- Return the number of maximal nonempty substrings containing no spaces.

### Examples
**Example 1**

- Input: `s = "Hello, my name is John"`
- Output: `5`

**Example 2**

- Input: `s = "Hello"`
- Output: `1`

**Example 3**

- Input: `s = "   "`
- Output: `0`

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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count transitions into non-space text**

A segment begins exactly where the current character is not a space and either it is at index zero or the previous character is a space. Count positions satisfying that condition during one left-to-right scan.

**Why one transition represents one whole segment**

Every maximal non-space run has one first character, and that character satisfies the start condition. No later character in the same run satisfies it because its predecessor is non-space. Conversely, every counted position begins a nonempty run that continues until a space or the string end, so the count is neither missing nor duplicating segments.

#### Complexity detail

The scan performs constant work for each of `n` characters, giving $O(n)$ time. A single integer counter uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Built-in split:** splitting on spaces and discarding empty pieces is concise but materializes $O(n)$ additional text.
- **Explicit in-segment flag:** track whether the previous position belongs to a segment; this is equivalent to checking the preceding character.
- **Walk backward at every character:** rediscovering each character's segment start is correct but takes $O(n^2)$ on one long segment.
- **Empty or all-space string:** no position starts a segment.
- **Repeated spaces:** only the first following non-space character is counted.
- **Punctuation:** punctuation is part of a segment because only the space character separates segments.

</details>

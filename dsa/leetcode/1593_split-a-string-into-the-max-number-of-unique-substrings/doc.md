# Split a String Into the Max Number of Unique Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1593 |
| Difficulty | Medium |
| Topics | Hash Table, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/) |

## Problem Description
### Goal
Given a string `s`, divide it into a list of non-empty substrings whose concatenation, in order, is exactly `s`. Every chosen piece must be a substring in the contiguous sense, so a split only places boundaries between existing adjacent characters; it may not reorder or omit characters.

The pieces in the resulting list must be pairwise unique. Different occurrences with the same text still count as equal and therefore cannot both appear in a valid split. Return the maximum number of pieces among all splits that satisfy this uniqueness rule.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters with $1 \le n \le 16$, where $n = \lvert s \rvert$.

**Return value**

Return the greatest possible number of pairwise distinct, non-empty substrings in a valid split of `s`.

### Examples
**Example 1**

- Input: `s = "ababccc"`
- Output: `5`
- Explanation: `"a"`, `"b"`, `"ab"`, `"c"`, and `"cc"` form one maximum valid split.

**Example 2**

- Input: `s = "aba"`
- Output: `2`
- Explanation: One valid maximum split is `"a"`, `"ba"`.

**Example 3**

- Input: `s = "aa"`
- Output: `1`

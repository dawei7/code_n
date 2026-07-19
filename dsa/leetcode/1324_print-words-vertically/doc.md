# Print Words Vertically

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1324 |
| Difficulty | Medium |
| Topics | Array, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/print-words-vertically/) |

## Problem Description
### Goal
Given a sentence `s`, place its words into columns in their original order and read the resulting character grid row by row. Each input word occupies exactly one column and appears from top to bottom.

When a word is shorter than a requested row, its column contributes a space so later words remain aligned. Remove spaces only from the end of each returned row; spaces before or between visible characters must be preserved.

Return all vertical rows from the first character position through the longest word's final position. The sentence contains uppercase English words separated by single spaces.

### Function Contract
**Inputs**

- `s`: a sentence of uppercase English words with one space between adjacent words and total length at most 200.

Let $w$ be the number of words, $L$ the maximum word length, and $P=wL$ the number of cells in the padded word rectangle.

**Return value**

A list of $L$ strings representing the rectangle's rows after trailing spaces are removed from each row.

### Examples
**Example 1**

- Input: `s = "HOW ARE YOU"`
- Output: `["HAY", "ORO", "WEU"]`

**Example 2**

- Input: `s = "TO BE OR NOT TO BE"`
- Output: `["TBONTB", "OEROOE", "   T"]`
- Explanation: The third row keeps its leading alignment spaces but has no trailing spaces.

**Example 3**

- Input: `s = "CONTEST IS COMING"`
- Output: `["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]`

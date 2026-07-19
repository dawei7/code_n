# Remove Comments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 722 |
| Difficulty | Medium |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-comments/) |

## Problem Description
### Goal
Given a C++ program as an array of source-code lines, remove its comments. `//` begins a line comment that discards itself and every character to its right on that line. `/*` begins a block comment that discards characters through the next `*/`, possibly across several source lines.

Comment markers inside an active block comment are ignored until its closing delimiter. Preserve all noncomment characters in order, joining code on opposite sides of a multiline block comment into the same output line, and return only nonempty resulting lines. The input guarantees that every opened block comment is closed.

### Function Contract
**Inputs**

- `source`: source-code lines without embedded newline characters; every opened block comment is eventually closed

**Return value**

- The nonempty source lines remaining after comment removal, with code on opposite sides of a multiline block comment joined into one output line

### Examples
**Example 1**

- Input: `source = ["int main() {","  // declaration","int x = 1;","}"]`
- Output: `["int main() {","  ","int x = 1;","}"]`

**Example 2**

- Input: `source = ["a/* comment","continued */b"]`
- Output: `["ab"]`

**Example 3**

- Input: `source = ["x/*one*/y/*two*/z"]`
- Output: `["xyz"]`

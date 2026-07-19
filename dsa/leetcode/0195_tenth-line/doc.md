# Tenth Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 195 |
| Difficulty | Easy |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/tenth-line/) |

## Problem Description
### Goal
Given the text file `file.txt`, count its lines from the beginning using one-based positions. Locate the line at position ten, where the first physical line is position one regardless of its text contents.

Write exactly the tenth line to standard output when it exists, preserving that line's content rather than splitting it into words. If the file contains fewer than ten lines, produce no output and no placeholder or error message. Earlier and later lines must not be printed. Keep the solution in the source-native Bash file-and-stdout form instead of converting it to a callable function.

### Function Contract
**Inputs**

- `file.txt`: a text file with zero or more lines

**Return value**

Write exactly the tenth line to stdout, or write nothing when the file has fewer than ten lines.

### Examples
**Example 1**

- File has lines `Line 1` through `Line 12`
- Output: `Line 10`

**Example 2**

- File has exactly ten lines
- Output: its final line

**Example 3**

- File has nine lines
- Output: nothing

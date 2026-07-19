# Valid Phone Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 193 |
| Difficulty | Easy |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-phone-numbers/) |

## Problem Description
### Goal
The file `file.txt` contains one candidate phone-number string per line. A line is valid only when the entire line matches either `xxx-xxx-xxxx` or `(xxx) xxx-xxxx`, where each `x` is a decimal digit and the spaces, hyphens, and parentheses occur exactly as shown.

Write every valid original line to standard output in its original file order. Reject lines with extra leading or trailing text, missing separators, misplaced whitespace, or the wrong number of digits, even if they contain a valid-looking fragment. Do not reformat accepted lines or print diagnostics for rejected ones; if no line matches, produce no output.

### Function Contract
**Inputs**

- `file.txt`: one candidate phone number per line

**Return value**

Write each original line matching `xxx-xxx-xxxx` or `(xxx) xxx-xxxx` to stdout, preserving file order.

### Examples
**Example 1**

- File lines: `987-123-4567`, `123 456 7890`, `(123) 456-7890`
- Output: the first and third lines

**Example 2**

- Line: `(555) 000-1234`
- Output: the same line

**Example 3**

- Line has an extra prefix or suffix
- Output: no line

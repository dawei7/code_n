# Word Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 192 |
| Difficulty | Medium |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/word-frequency/) |

## Problem Description
### Goal
The file `words.txt` contains lowercase words separated by spaces or line breaks. Treat every whitespace-delimited token as one word and count how many times each distinct word occurs across the complete file, regardless of which line contains it.

Write one line to standard output for each distinct word in the form `word count`, using one space between the token and its decimal frequency. Sort the lines in descending order by frequency, and do not emit headers, punctuation, or duplicate summary rows. An empty file produces no output. Preserve shell-style file input and stdout behavior rather than reframing the task as a function call.

### Function Contract
**Inputs**

- `words.txt`: lowercase words separated by spaces or line breaks

**Return value**

Write one `word count` pair per line to stdout, ordered by decreasing count.

### Examples
**Example 1**

- File: `the day is sunny the the the sunny is is`
- Output starts with: `the 4`, then `is 3`, then `sunny 2`, then `day 1`

**Example 2**

- File: `code`
- Output: `code 1`

**Example 3**

- File contains words across multiple lines
- Output: counts combine all lines

# Goal Parser Interpretation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1678 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/goal-parser-interpretation/) |

## Problem Description
### Goal

A Goal Parser receives a command formed by concatenating tokens from the fixed alphabet `"G"`, `"()"`, and `"(al)"`. The input is guaranteed to be a valid sequence of those complete tokens, so parentheses never appear in any other form and no validation or error recovery is required.

Interpret each `"G"` as `"G"`, each `"()"` as `"o"`, and each `"(al)"` as `"al"`. Concatenate the decoded pieces in the same order in which their tokens occur and return the resulting string. Token boundaries matter only while reading the command; they do not appear in the output.

### Function Contract
**Inputs**

- `command`: a string of length $n$ formed by concatenating one or more valid tokens from `"G"`, `"()"`, and `"(al)"`

**Return value**

The string obtained by decoding every token in order.

### Examples
**Example 1**

- Input: `command = "G()(al)"`
- Output: `"Goal"`

**Example 2**

- Input: `command = "G()()()()(al)"`
- Output: `"Gooooal"`

**Example 3**

- Input: `command = "(al)G(al)()()G"`
- Output: `"alGalooG"`

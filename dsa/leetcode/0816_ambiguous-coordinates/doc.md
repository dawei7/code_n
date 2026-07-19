# Ambiguous Coordinates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 816 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ambiguous-coordinates/) |

## Problem Description

### Goal

A coordinate pair was originally written as `(x, y)`, but its comma, decimal points, and spaces were erased while the outer parentheses and digit order remained. Given that compressed string, reconstruct every coordinate that could have produced it by restoring exactly one comma and optionally one decimal point on either side.

Each restored number must use ordinary decimal notation: a multi-digit integer part cannot begin with `0`, and a fractional part cannot end with `0`. Forms such as `00`, `01`, `1.0`, `.5`, and `5.` are therefore invalid, while `0`, `0.5`, and `10` are valid. Return every valid formatted pair; their order does not matter.

### Function Contract

**Inputs**

- `s`: a string of digits enclosed in parentheses. Its interior contains between two and ten digits.

**Return value**

- All possible strings in the form `(x, y)`, in any order, where neither number has an invalid leading zero, and a fractional number has no trailing zero.

### Examples

**Example 1**

- Input: `s = "(123)"`
- Output: `["(1, 23)","(1, 2.3)","(12, 3)","(1.2, 3)"]`
- Explanation: Each interior split supplies the comma, and each side may contain at most one legal decimal point.

**Example 2**

- Input: `s = "(00011)"`
- Output: `["(0, 0.011)","(0.001, 1)"]`
- Explanation: Leading-zero rules eliminate every other placement.

**Example 3**

- Input: `s = "(0123)"`
- Output: `["(0, 123)","(0, 12.3)","(0, 1.23)","(0.1, 23)","(0.1, 2.3)","(0.12, 3)"]`
- Explanation: A multi-digit whole part cannot begin with zero, but `0` followed by a nonzero fractional suffix is valid.

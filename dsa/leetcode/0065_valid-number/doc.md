# Valid Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 65 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-number/) |

## Problem Description
### Goal
You are given a nonempty string and must decide whether the entire string is a valid decimal number. A valid mantissa may have an optional leading sign and may be an integer or decimal, but it must contain at least one digit; forms such as `2`, `-0.1`, `4.`, and `.9` are permitted.

The mantissa may be followed by one `e` or `E` and an exponent. An exponent may have its own sign but must be an integer containing at least one digit. No spaces, extra characters, misplaced signs, repeated decimal points, or decimal exponent parts are accepted. Return the resulting boolean classification.

### Function Contract
**Inputs**

- `s`: a nonempty string to classify

**Return value**

`True` if the entire string is a valid number and `False` otherwise.

### Examples
**Example 1**

- Input: `s = "2"`
- Output: `True`

**Example 2**

- Input: `s = "-90E3"`
- Output: `True`

**Example 3**

- Input: `s = "99e2.5"`
- Output: `False`

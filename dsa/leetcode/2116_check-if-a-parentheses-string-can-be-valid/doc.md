# Check if a Parentheses String Can Be Valid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2116 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) |

## Problem Description
### Goal

A nonempty parentheses string contains only `(` and `)`. It is valid when its
parentheses can be paired correctly: `()` is valid, concatenating two valid
strings remains valid, and enclosing a valid string in one matching pair also
produces a valid string.

You are given equal-length strings `s` and `locked`. At index `i`, a `1` in
`locked` fixes `s[i]` and forbids changing it. A `0` makes that position
editable, so its character may be chosen as either `(` or `)`.

Determine whether some assignment of every editable position makes the whole
string a valid parentheses string.

### Function Contract
**Inputs**

- `s`: A nonempty string containing only `(` and `)`.
- `locked`: A binary string with the same length as `s`; `1` fixes the
  corresponding character and `0` permits either parenthesis.

Let $n = \lvert s\rvert = \lvert\texttt{locked}\rvert$.

**Return value**

Return `true` if the editable positions can be assigned to form a valid
parentheses string; otherwise, return `false`.

### Examples
**Example 1**

- Input: `s = "))()))", locked = "010100"`
- Output: `true`

Changing positions zero and four to `(` yields a valid assignment.

**Example 2**

- Input: `s = "()()", locked = "0000"`
- Output: `true`

The current characters already form one valid choice.

**Example 3**

- Input: `s = ")", locked = "0"`
- Output: `false`

Every valid parentheses string has even length.

**Example 4**

- Input: `s = "(((())(((())", locked = "111111010111"`
- Output: `true`

The two editable positions can both be changed to closing parentheses.

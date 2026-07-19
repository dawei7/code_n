# Remove Outermost Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1021 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-outermost-parentheses/) |

## Problem Description

### Goal

A valid parentheses string is empty, encloses another valid string as `"(" + A + ")"`, or concatenates valid strings as `A + B`. A nonempty valid string is primitive when it cannot be split into two nonempty valid parentheses strings.

You are given a valid parentheses string `s`. Decompose it uniquely into consecutive primitive strings, remove the outermost opening and closing parenthesis from every primitive, and return the concatenation of what remains. A primitive equal to `"()"` contributes an empty string.

### Function Contract

**Inputs**

- `s`: a valid parentheses string of length $N$, where $1\le N\le10^5$ and every character is `"("` or `")"`.

**Return value**

- The string obtained after deleting the outermost pair from each primitive component.

### Examples

**Example 1**

- Input: `s = "(()())(())"`
- Output: `"()()()"`
- Explanation: `"(()())" + "(())"` becomes `"()()" + "()"`.

**Example 2**

- Input: `s = "(()())(())(()(()))"`
- Output: `"()()()()(())"`
- Explanation: Removing the outer pair from its three primitives yields `"()()"`, `"()"`, and `"()(())"`.

**Example 3**

- Input: `s = "()()"`
- Output: `""`
- Explanation: Both primitives are `"()"`, so both become empty.

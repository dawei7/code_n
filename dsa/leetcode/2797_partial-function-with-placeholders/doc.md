# Partial Function with Placeholders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2797 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/partial-function-with-placeholders/) |

## Problem Description

### Goal

Given a function `fn` and an array of partially supplied arguments, create a new function. An entry equal to the string `"_"` is a placeholder rather than a fixed argument.

When the returned function is called, consume its arguments from left to right to replace the placeholders in the captured array. If call-time arguments remain after every placeholder is filled, append those values to the end. Invoke `fn` with the completed sequence passed as separate arguments and return its result.

### Function Contract

**Inputs**

- `fn`: The function that the returned partial function eventually invokes.
- `args`: A valid JSON array containing fixed values and zero or more `"_"` placeholders, with $1 \le \lvert\texttt{args}\rvert \le 5 \cdot 10^4$.

The returned function accepts a valid JSON sequence `restArgs` with length between $1$ and $5 \cdot 10^4$. The number of placeholders in `args` does not exceed the number of supplied `restArgs`.

**Return value**

Return a function that fills placeholders, appends unused call-time arguments, invokes `fn` with the merged values as separate arguments, and returns the value produced by `fn`.

### Examples

**Example 1**

- Input: `fn = (...values) => values`, `args = [2, 4, 6]`, `restArgs = [8, 10]`
- Output: `[2, 4, 6, 8, 10]`
- Explanation: There are no placeholders, so both call-time values are appended.

**Example 2**

- Input: `fn = (...values) => values`, `args = [1, 2, "_", 4, "_", 6]`, `restArgs = [3, 5]`
- Output: `[1, 2, 3, 4, 5, 6]`
- Explanation: The two call-time values replace the two placeholders in order.

**Example 3**

- Input: `fn = (a, b, c) => b + a - c`, `args = ["_", 5]`, `restArgs = [5, 20]`
- Output: `-10`
- Explanation: The first value fills the placeholder, the second is appended, and `fn(5, 5, 20)` returns `-10`.

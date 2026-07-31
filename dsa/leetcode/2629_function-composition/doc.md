# Function Composition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2629 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/function-composition/) |

## Problem Description

### Goal

Given an array of single-argument integer functions, return one new function representing their composition.

Composition evaluates the functions from right to left. For an array `[f, g, h]`, the returned function must compute `f(g(h(x)))`: `h` receives the original input, `g` receives the result from `h`, and `f` receives the result from `g`.

When the array contains no functions, its composition is the identity function, so calling the returned function must produce its input unchanged. Every supplied function accepts one integer and returns one integer.

### Function Contract

**Inputs**

- `functions`: An array of zero to $1000$ functions, each mapping one integer to one integer.

The returned function receives an integer `x` with $-1000 \le x \le 1000$. Let $n$ be the length of `functions`.

**Return value**

Return a function that applies every function in `functions` exactly once from the last array position to the first and returns the final value. With $n = 0$, return the identity behavior.

### Examples

**Example 1**

- Input: `functions = [x => x + 1, x => x * x, x => 2 * x]`, `x = 4`
- Output: `65`
- Explanation: Right-to-left evaluation produces `8`, then `64`, then `65`.

**Example 2**

- Input: `functions = [x => 10 * x, x => 10 * x, x => 10 * x]`, `x = 1`
- Output: `1000`
- Explanation: Each of the three functions multiplies the current value by ten.

**Example 3**

- Input: `functions = []`, `x = 42`
- Output: `42`
- Explanation: The composition of an empty function array is the identity function.

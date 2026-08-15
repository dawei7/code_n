# Memoize

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2623 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/memoize/) |

## Problem Description

### Goal

Given a JavaScript function `fn`, return a memoized version that evaluates `fn` at most once for each exact tuple of arguments. On the first call with a tuple, invoke `fn`, save its return value, and return it. Later calls with the same ordered arguments must return the saved value without invoking `fn` again.

The possible functions are `sum(a, b)`, recursive `fib(n)`, and recursive `factorial(n)`. Argument order is significant: `(3, 2)` and `(2, 3)` are different cache keys even though `sum` gives them the same result. Values for `a` and `b` are between $0$ and $10^5$, while `n` is between $1$ and $10$.

### Function Contract

**Inputs**

- `fn`: One of the supported numeric functions to wrap.
- `args`: The ordered numeric arguments supplied to each invocation of the returned function.

The local adapter also receives `fnName`, `actions`, and `values` to run calls and inspect how often the original function executes.

**Return value**

Return a function that produces the same value as `fn` for every argument tuple while invoking `fn` only on the tuple's first occurrence.

### Examples

#### Example 1

- **Input:** memoized `sum`, called with `(2, 2)`, `(2, 2)`, then `(1, 2)`
- **Output:** `[4, 4, 3]`, with original call counts `1` and then `2`
- **Explanation:** The repeated `(2, 2)` call uses the cached result.

#### Example 2

- **Input:** memoized `factorial`, called with `2`, `3`, `2`, then `3`
- **Output:** `[2, 6, 2, 6]`
- **Explanation:** Only the first call for each distinct argument invokes the original function.

#### Example 3

- **Input:** memoized `fib`, called with `5`
- **Output:** `8`, with original call count `1`
- **Explanation:** Memoization applies to calls of the wrapper; recursion inside the supplied `fib` function remains part of that one underlying invocation.

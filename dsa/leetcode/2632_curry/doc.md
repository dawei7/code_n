# Curry

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2632 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/curry/) |

## Problem Description

### Goal

Given a JavaScript function `fn`, return a curried version of it. The returned function may receive any number of the original parameters at a time, including none. Until enough parameters have been collected, a call returns another curried function; once the original arity is reached, it returns the value that `fn` would produce from all collected arguments in order.

For example, if `sum` expects three arguments, `csum(1)(2)(3)`, `csum(1, 2)(3)`, `csum(1)(2, 3)`, and `csum(1, 2, 3)` must all behave like `sum(1, 2, 3)`. Empty calls do not change the collected sequence. If `fn.length` is zero, invoking the curried function with no arguments must immediately evaluate `fn`.

### Function Contract

**Inputs**

- `fn`: A function whose parameters are explicitly declared.

The test driver supplies a sequence `inputs` of between $1$ and $1000$ argument arrays. Each numeric argument lies between $0$ and $10^5$, the total number of arguments equals `fn.length`, and $0 \le \texttt{fn.length} \le 1000$. When the arity is positive, the final input group is nonempty. For zero arity, the sequence is exactly `[[]]`.

Let $n$ be the number of collected arguments and $p$ the number of calls in the sequence.

**Return value**

Return a curried function. Each partial call returns another function carrying the preceding arguments; the call that reaches the original arity returns `fn` evaluated with the complete ordered argument list.

### Examples

**Example 1**

- Input: `fn = (a, b, c) => a + b + c`, `inputs = [[1], [2], [3]]`
- Output: `6`
- Explanation: Three one-argument calls collectively supply the three declared parameters.

**Example 2**

- Input: `fn = (a, b, c) => a + b + c`, `inputs = [[1, 2], [3]]`
- Output: `6`
- Explanation: The first call supplies two parameters and the second completes the invocation.

**Example 3**

- Input: `fn = (a, b, c) => a + b + c`, `inputs = [[], [], [1, 2, 3]]`
- Output: `6`
- Explanation: Empty calls preserve the pending curry without adding arguments.

**Example 4**

- Input: `fn = () => 42`, `inputs = [[]]`
- Output: `42`
- Explanation: Calling a curried zero-parameter function evaluates the original immediately.

# Allow One Function Call

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2666 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Closure, Higher-Order Function |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/allow-one-function-call/) |

## Problem Description

### Goal

Given a function `fn`, return a new function with the same call interface but permission to invoke `fn` at most once.

On its first invocation, the returned function must forward the supplied arguments to `fn` and return `fn`'s result. On every later invocation, it must skip `fn` entirely and return `undefined`. The once-only state belongs to the returned wrapper; creating another wrapper starts with a fresh unused state.

### Function Contract

**Inputs**

- `fn`: The function whose execution must be limited to one call.

The test harness supplies between 1 and 10 argument arrays. Each call contains between 1 and 100 JSON-compatible arguments, and the serialized calls contain at most 1000 characters.

**Return value**

- Return a function that forwards the first invocation and returns `undefined` without invoking `fn` thereafter.

The app-local harness records only the defined first result together with the underlying function's call count.

### Examples

**Example 1**

- Input: `fn = sum, calls = [[1,2,3],[2,3,6]]`
- Output: `[{"calls":1,"value":6}]`
- Explanation: The first call evaluates the sum. The second returns `undefined`, and the original function's call count remains one.

**Example 2**

- Input: `fn = product, calls = [[5,7,4],[2,3,6],[4,6,8]]`
- Output: `[{"calls":1,"value":140}]`
- Explanation: Only the first argument list reaches the multiplication function.

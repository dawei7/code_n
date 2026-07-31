# Create Hello World Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2667 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Closure, Higher-Order Function |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/create-hello-world-function/) |

## Problem Description

### Goal

Write a function `createHelloWorld` that returns another function. Every invocation of the returned function must produce the exact string `"Hello World"`.

The returned function may receive any number of arguments, including none, but neither their values nor their types may change the result.

Creating the function and calling it are separate operations: `createHelloWorld()` produces the callable, and that callable may then be invoked repeatedly. Every invocation is independent of earlier calls and must return the same exact, case-sensitive text without adding punctuation or whitespace.

### Function Contract

**Inputs**

`createHelloWorld` takes no required parameters. The function it returns may be called with an `args` sequence containing from zero to ten arbitrary JSON-compatible values.

**Return value**

- Return a function that always returns the exact case-sensitive string `"Hello World"`.

### Examples

**Example 1**

- Input: `args = []`
- Output: `"Hello World"`
- Explanation: Calling the returned function without arguments produces the required constant.

**Example 2**

- Input: `args = [{},null,42]`
- Output: `"Hello World"`
- Explanation: Objects, null values, numbers, and every other supplied argument are ignored.

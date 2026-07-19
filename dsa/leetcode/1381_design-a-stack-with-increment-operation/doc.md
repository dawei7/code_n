# Design a Stack With Increment Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/design-a-stack-with-increment-operation/) |

## Problem Description

### Goal

Design a stack with a fixed maximum capacity. It supports ordinary `push` and `pop` operations together with an operation that adds a value to the bottom part of the current stack.

A push adds a value only when the stack is not full; otherwise it changes nothing. A pop removes and returns the top value, or returns `-1` when the stack is empty. An `increment(k, val)` call adds `val` to each of the bottom `min(k, current size)` elements.

### Function Contract

**Inputs**

- `max_size`: the positive stack capacity supplied to the constructor.
- `operations`: at most $1000$ calls encoded as `[method, args]` pairs, where `method` is `push`, `pop`, or `increment`.

**Return value**

- A list containing each method result in call order. `push` and `increment` contribute `null`; `pop` contributes the removed value or `-1`.

### Examples

**Example 1**

- Input: `max_size = 2, operations = [["push",[1]],["push",[2]],["pop",[]]]`
- Output: `[null,null,2]`

**Example 2**

- Input: `max_size = 3, operations = [["push",[1]],["push",[2]],["increment",[2,5]],["pop",[]]]`
- Output: `[null,null,null,7]`

**Example 3**

- Input: `max_size = 1, operations = [["pop",[]]]`
- Output: `[-1]`

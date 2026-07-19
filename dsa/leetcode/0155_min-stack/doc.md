# Min Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Stack, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/min-stack/) |

## Problem Description
### Goal
Implement a stack of integers with the usual last-in, first-out behavior plus direct access to its current minimum. `push(val)` adds a value, `pop()` removes the most recently added remaining value, and `top()` returns that value without removing it.

`getMin()` must return the smallest value currently stored, including repeated minima that remain after only one copy is popped. Process the operation sequence in order and return one aligned result per call, using `None` for construction and mutating operations. All four methods must run in constant time; calls that inspect or remove a value are guaranteed to occur only when the stack is nonempty.

### Function Contract
**Inputs**

- `operations`: method names beginning with `MinStack`, followed by `push`, `pop`, `top`, and `getMin`
- `arguments`: one argument list per operation; only `push` receives an integer

**Return value**

A result list aligned with the operations: `None` for construction, push, and pop; the requested integer for top and getMin.

### Examples
**Example 1**

- Input: construct, `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`
- Output: `[null,null,null,null,-3,null,0,-2]`

**Example 2**

- Input: construct, `push(1)`, `getMin()`, `top()`
- Output: `[null,null,1,1]`

**Example 3**

- Input: push two equal minimum values and pop one
- Output: the remaining equal value is still the minimum

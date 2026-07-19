# Implement Queue using Stacks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Design, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) |

## Problem Description
### Goal
Implement a first-in, first-out queue while using only stack-style storage operations. `push(x)` adds an integer at the back, `pop()` removes and returns the oldest remaining value at the front, and `peek()` returns that front value without removing it.

`empty()` reports whether the queue currently contains no values. Process all commands against one persistent queue state and return aligned operation results, using `null` for pushes. Calls that inspect or remove a front value occur only when the queue is nonempty. Internally, use only ordinary stack actions such as pushing, popping, top inspection, size, and emptiness rather than substituting a native queue.

### Function Contract
**Inputs**

- `operations`: method names chosen from `push`, `pop`, `peek`, and `empty`
- `values`: the corresponding pushed integer, or `null` for an operation with no argument

**Return value**

The result of every operation in order: `null` for `push`, the affected value for `pop` or `peek`, and a boolean for `empty`.

### Examples
**Example 1**

- Input: `operations = ["push","push","peek","pop","empty"], values = [1,2,null,null,null]`
- Output: `[null,null,1,1,false]`

**Example 2**

- Input: `operations = ["empty","push","pop","empty"], values = [null,7,null,null]`
- Output: `[true,null,7,true]`

**Example 3**

- Input: `operations = ["push","peek","peek"], values = [4,null,null]`
- Output: `[null,4,4]`

# Build an Array With Stack Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1441 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/build-an-array-with-stack-operations/) |

## Problem Description

### Goal

A stream supplies the integers from `1` through `n` in increasing order. Reading the next stream value and placing it on an initially empty stack is recorded as `"Push"`. Removing the stack's top value is recorded as `"Pop"`.

Return a sequence of those operation names that makes the final stack equal `target` from bottom to top. Every read value must first be pushed, unwanted values may then be popped, and reading must stop as soon as the target has been built. The target is strictly increasing, so its order is compatible with the stream.

### Function Contract

**Inputs**

- `target`: a strictly increasing integer array of length $t$, where $1 \le t \le 100$.
- `n`: the stream's upper value, where $1 \le n \le 100$ and `target[t - 1] <= n`.
- Let $L=\texttt{target[t-1]}$ be the final stream value that must be read.

**Return value**

- A list containing `"Push"` and `"Pop"` operations that builds `target` and stops immediately after reading $L$.

### Examples

**Example 1**

- Input: `target = [1,3], n = 3`
- Output: `["Push","Push","Pop","Push"]`

**Example 2**

- Input: `target = [1,2,3], n = 3`
- Output: `["Push","Push","Push"]`

**Example 3**

- Input: `target = [2,3,4], n = 4`
- Output: `["Push","Pop","Push","Push","Push"]`

# Counter II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2665 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Closure, Object |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/counter-ii/) |

## Problem Description

### Goal

Write a function `createCounter` that accepts an initial integer `init` and returns an object containing three stateful functions:

- `increment()` adds $1$ to the current value and returns the updated value.
- `decrement()` subtracts $1$ from the current value and returns the updated value.
- `reset()` restores the current value to the original `init` and returns it.

All three functions belonging to one returned object operate on the same private current value. Calling `reset()` must always use the original initialization value, regardless of how many updates have occurred.

### Function Contract

**Inputs**

- `init`: The counter's initial integer, where $-1000 \le \texttt{init} \le 1000$.

For the app-local harness, `calls` is a sequence of zero to 1000 strings, each equal to `"increment"`, `"decrement"`, or `"reset"`, applied in order to one counter instance.

**Return value**

- `createCounter(init)` returns an object exposing the three required functions.
- The app-local harness returns the numeric result of every requested call in order.

### Examples

#### Example 1

- **Input:** `init = 5, calls = ["increment","reset","decrement"]`
- **Output:** `[6,5,4]`
- **Explanation:** Increment changes the value to `6`, reset restores `5`, and decrement then changes it to `4`.

#### Example 2

- **Input:** `init = 0, calls = ["increment","increment","decrement","reset","reset"]`
- **Output:** `[1,2,1,0,0]`
- **Explanation:** Updates share one current value, while either reset returns to the unchanged original value `0`.

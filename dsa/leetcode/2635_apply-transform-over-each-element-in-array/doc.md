# Apply Transform Over Each Element in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2635 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/) |

## Problem Description

### Goal

Given an integer array `arr` and a mapping callback `fn`, create a new array by applying the callback to every source element. The callback receives both the current value and its numeric index.

For each valid position $i$, the result must satisfy `returnedArray[i] = fn(arr[i], i)`. Preserve the source length and positional order, and implement the transformation without calling the built-in `Array.map` method.

### Function Contract

**Inputs**

- `arr`: An integer array of length $n$, where $0 \le n \le 1000$ and each value lies between $-10^9$ and $10^9$.
- `fn`: A callback accepting a source value and its index and returning an integer.

For the app-local serializable adapter, `fnName` selects an authored transformation and `fnArg` provides an optional constant or multiplier. Benchmarks may create a legal increasing range through `arrPlan`.

**Return value**

Return a new length-$n$ array whose value at every index $i$ is `fn(arr[i], i)`. Do not mutate `arr` or use `Array.map`.

### Examples

#### Example 1

- **Input:** `arr = [1,2,3]`, `fn = n => n + 1`
- **Output:** `[2,3,4]`
- **Explanation:** One is added independently to every source value.

#### Example 2

- **Input:** `arr = [1,2,3]`, `fn = (n, i) => n + i`
- **Output:** `[1,3,5]`
- **Explanation:** Each value is increased by its own zero-based index.

#### Example 3

- **Input:** `arr = [10,20,30]`, `fn = () => 42`
- **Output:** `[42,42,42]`
- **Explanation:** A callback may ignore both arguments and return the same integer for every position.

# Array Reduce Transformation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2626 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/array-reduce-transformation/) |

## Problem Description

### Goal

Given an integer array `nums`, a reducer function `fn`, and an initial accumulator `init`, combine the array into one final value.

Process the elements sequentially from left to right. The first call receives `init` and `nums[0]`. Every later call receives the previous call's return value and the next array element. After the last element, return the current accumulator.

If `nums` is empty, no reducer call is made and the answer is `init`. Implement the transformation without using JavaScript's built-in `Array.reduce` method.

### Function Contract

**Inputs**

- `nums`: An integer array with length from $0$ through $1000$; every element is between $0$ and $1000$.
- `fn`: A reducer function that accepts the current accumulator followed by the current array element and returns the next accumulator.
- `init`: The initial accumulator value, between $0$ and $1000$.

Let $n$ be the length of `nums`.

**Return value**

Return the accumulator obtained after applying `fn` once to each element in left-to-right order, or return `init` unchanged when $n = 0$.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4]`, `fn = (accum, curr) => accum + curr`, `init = 0`
- Output: `10`
- Explanation: The accumulator progresses through `1`, `3`, `6`, and `10`.

**Example 2**

- Input: `nums = [1,2,3,4]`, `fn = (accum, curr) => accum + curr * curr`, `init = 100`
- Output: `130`
- Explanation: The four squared values add `1 + 4 + 9 + 16` to the initial value.

**Example 3**

- Input: `nums = []`, `fn = (accum, curr) => 0`, `init = 25`
- Output: `25`
- Explanation: The reducer is never called for an empty array, so the initial value is returned.

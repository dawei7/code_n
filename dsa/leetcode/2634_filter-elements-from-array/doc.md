# Filter Elements from Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2634 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/filter-elements-from-array/) |

## Problem Description

### Goal

Given an integer array `arr` and a filtering callback `fn`, construct a new array containing exactly the source elements whose callback results are truthy. The callback receives the current value as its first argument and may use the current index as its second argument.

For every source position $i$, retain `arr[i]` precisely when `Boolean(fn(arr[i], i))` is `true`. The retained elements must remain in their original relative order. Implement this behavior directly without calling the built-in `Array.filter` method.

### Function Contract

**Inputs**

- `arr`: An integer array of length $n$, where $0 \le n \le 1000$ and every value lies between $-10^9$ and $10^9$.
- `fn`: A callback accepting `arr[i]` and optionally its numeric index `i`.

For the app-local serializable adapter, `fnName` selects an authored callback and `fnArg` supplies an optional threshold. Benchmarks may construct a legal increasing range through `arrPlan`.

**Return value**

Return a new array containing each `arr[i]` for which `fn(arr[i], i)` is truthy, in source order. Do not mutate `arr` or use `Array.filter`.

### Examples

**Example 1**

- Input: `arr = [0,10,20,30]`, `fn = n => n > 10`
- Output: `[20,30]`
- Explanation: Only twenty and thirty are strictly greater than ten.

**Example 2**

- Input: `arr = [1,2,3]`, `fn = (n, i) => i === 0`
- Output: `[1]`
- Explanation: The callback keeps only the element at index zero.

**Example 3**

- Input: `arr = [-2,-1,0,1,2]`, `fn = n => n + 1`
- Output: `[-2,0,1,2]`
- Explanation: The callback returns zero only for `-1`; zero is falsy, while the other numeric results are truthy.

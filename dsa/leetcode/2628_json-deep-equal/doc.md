# JSON Deep Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2628 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/json-deep-equal/) |

## Problem Description

### Goal

Given two valid JSON values `o1` and `o2`, determine whether they are deeply equal.

Primitive values are deeply equal only when JavaScript's strict equality operator `===` considers them equal. Arrays must have the same length, contain corresponding elements in the same order, and have deeply equal values at every position. Objects must have exactly the same set of keys, regardless of key insertion order, and the values associated with each key must be deeply equal.

The values may be `null`, booleans, numbers, strings, arrays, or objects because both originate from `JSON.parse`. Arrays and ordinary objects are distinct JSON structures even when their enumerable property names and values look alike. Implement the comparison without using Lodash's `_.isEqual` function.

### Function Contract

**Inputs**

- `o1`: The first valid JSON value.
- `o2`: The second valid JSON value.

Each value's serialized JSON length is between $1$ and $10^5$, and the maximum nesting depth is at most $1000$.

Let $n$ be the total number of primitive values, array entries, and object properties inspected before the comparison finishes, and let $d$ be the greatest nesting depth reached.

**Return value**

Return `true` exactly when `o1` and `o2` have the same JSON type and recursively equal contents under the rules above; otherwise return `false`.

### Examples

**Example 1**

- Input: `o1 = {"x":1,"y":2}`, `o2 = {"x":1,"y":2}`
- Output: `true`
- Explanation: Both objects contain the same keys with equal associated numbers.

**Example 2**

- Input: `o1 = {"y":2,"x":1}`, `o2 = {"x":1,"y":2}`
- Output: `true`
- Explanation: Object key order does not affect equality.

**Example 3**

- Input: `o1 = {"x":null,"L":[1,2,3]}`, `o2 = {"x":null,"L":["1","2","3"]}`
- Output: `false`
- Explanation: Numbers and their string representations are different primitive values.

**Example 4**

- Input: `o1 = true`, `o2 = false`
- Output: `false`
- Explanation: The two booleans fail strict equality.

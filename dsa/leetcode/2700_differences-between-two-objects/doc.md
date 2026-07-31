# Differences Between Two Objects

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2700 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/differences-between-two-objects/) |

## Problem Description

### Goal

Given two deeply nested JavaScript objects or arrays, `obj1` and `obj2`, construct a new object describing only the values that differ at keys present in both inputs. Both inputs are values that could be produced by `JSON.parse`.

When the two values at a shared key are different primitive values, or when one is an array and the other is an object, store the leaf difference as `[valueFromObj1, valueFromObj2]`. When both values are arrays or both are objects, compare them recursively and retain only descendants that contain a difference.

Keys found in only one input are ignored. Array indices act as keys, so elements beyond the shorter array are likewise omitted. Object property order does not affect the result.

### Function Contract

**Inputs**

- `obj1`: A JSON object or array whose serialized length is between $2$ and $10^4$.
- `obj2`: Another JSON object or array with the same serialized-length bound.

**Return value**

Return a nested object whose leaves are two-element difference arrays. Omit unchanged branches and keys missing from either side; return `{}` when no retained difference exists.

### Examples

**Example 1**

- Input: `obj1 = {}`, `obj2 = {"a":1,"b":2}`
- Output: `{}`
- Explanation: The two keys exist only in `obj2`, so neither is compared.

**Example 2**

- Input: `obj1 = {"a":1,"v":3,"x":[],"z":{"a":null}}`, `obj2 = {"a":2,"v":4,"x":[],"z":{"a":2}}`
- Output: `{"a":[1,2],"v":[3,4],"z":{"a":[null,2]}}`

**Example 3**

- Input: `obj1 = {"a":5,"v":6,"z":[1,2,4,[2,5,7]]}`, `obj2 = {"a":5,"v":7,"z":[1,2,3,[1]]}`
- Output: `{"v":[6,7],"z":{"2":[4,3],"3":{"0":[2,1]}}}`
- Explanation: Array indices $2$ and $3$ differ. Removed tail indices are ignored.

**Example 4**

- Input: `obj1 = {"a":{"b":1}}`, `obj2 = {"a":[5]}`
- Output: `{"a":[{"b":1},[5]]}`
- Explanation: An object and an array are different container types, so the entire values form one leaf difference.

**Example 5**

- Input: `obj1 = {"a":[1,2,{}],"b":false}`, `obj2 = {"b":false,"a":[1,2,{}]}`
- Output: `{}`
- Explanation: The structures are equal despite their different property order.

# Make Object Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2692 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/make-object-immutable/) |

## Problem Description

### Goal

Given a JSON object or array, return an immutable view of the same data. Reading properties, traversing nested containers, enumerating keys, and using non-mutating behavior must continue to work. Any attempted alteration must instead throw the exact required string literal; it must not throw an `Error` object and must not change the original JSON value.

Assigning or otherwise modifying a property of an object throws `"Error Modifying: key"`. Modifying an array index throws `"Error Modifying Index: index"`. Calling any mutating array method—`pop`, `push`, `shift`, `unshift`, `splice`, `sort`, or `reverse`—throws `"Error Calling Method: methodName"`. Nested objects and arrays require the same protection as the root.

### Function Contract

**Inputs**

- `obj`: A valid JSON object or array whose serialized length is from 2 through $10^5$.
- `action`: The app-local adapter's description of one read, key enumeration, assignment, deletion, property definition, or array-method call performed against the immutable view.

**Return value**

The native `makeImmutable(obj)` returns a deeply protected view of `obj`. The app-local `solve(obj, action)` executes the requested interaction and returns `{value, error}`, with `error` holding a caught string literal and `value` set to `null` when an operation is rejected.

### Examples

#### Example 1

- **Input:** `obj = {"x":5}` followed by assigning `obj.x = 5`.
- **Output:** `{"value":null,"error":"Error Modifying: x"}`

#### Example 2

- **Input:** `obj = [1,2,3]` followed by assigning index `1`.
- **Output:** `{"value":null,"error":"Error Modifying Index: 1"}`

#### Example 3

- **Input:** `obj = {"arr":[1,2,3]}` followed by calling `obj.arr.push(4)`.
- **Output:** `{"value":null,"error":"Error Calling Method: push"}`

#### Example 4

- **Input:** `obj = {"x":2,"y":2}` followed by `Object.keys(obj)`.
- **Output:** `{"value":["x","y"],"error":null}`

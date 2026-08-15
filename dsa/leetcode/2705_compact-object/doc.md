# Compact Object

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2705 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/compact-object/) |

## Problem Description

### Goal

Given a JavaScript object or array `obj` produced by `JSON.parse`, construct its compact form. Remove every property or array element whose value is falsy according to `Boolean(value)`, and apply the same operation recursively inside every retained nested object and array.

Arrays are treated as collections whose indices are keys, but removing an element must close the gap in the returned array. A truthy container remains present even if all of its contents are removed, so an input such as `[0]` nested inside another array becomes `[]` rather than disappearing. Return the fully compacted structure without changing the original value's object-versus-array shape.

### Function Contract

**Inputs**

- `obj`: A valid JSON object or array whose serialized length is between $2$ and $10^6$ characters.

**Return value**

Return a new object or array with every falsy value removed at every nesting level. Preserve truthy primitive values, retained object keys, array order, and empty containers that result from recursive compaction.

### Examples

#### Example 1

- **Input:** `obj = [null,0,false,1]`
- **Output:** `[1]`
- **Explanation:** The first three array elements are falsy and are removed.

#### Example 2

- **Input:** `obj = {"a":null,"b":[false,1]}`
- **Output:** `{"b":[1]}`
- **Explanation:** Property `a` and the first element inside `b` are falsy.

#### Example 3

- **Input:** `obj = [null,0,5,[0],[false,16]]`
- **Output:** `[5,[],[16]]`
- **Explanation:** Both nested arrays are truthy containers, so they remain after their falsy elements are removed.

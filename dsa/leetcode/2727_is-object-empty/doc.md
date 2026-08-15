# Is Object Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2727 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/is-object-empty/) |

## Problem Description

### Goal

Given either a JSON object or a JSON array, determine whether it is empty. An object is empty exactly when it contains no key-value pairs, while an array is empty exactly when it contains no elements.

The input can be treated as the result of `JSON.parse`, so its observable contents are ordinary JSON properties or array indices rather than custom prototype behavior. Values such as `null`, `false`, and `0` still count as elements or property values; emptiness depends on presence, not truthiness.

### Function Contract

**Inputs**

- `obj`: A valid JSON object or array whose serialized length is between $2$ and $10^5$ characters.

**Return value**

Return `true` when the object has no key-value pair or the array has no element; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `obj = {"x":5,"y":42}`
- **Output:** `false`
- **Explanation:** The object contains two key-value pairs.

#### Example 2

- **Input:** `obj = {}`
- **Output:** `true`
- **Explanation:** No property is present.

#### Example 3

- **Input:** `obj = [null,false,0]`
- **Output:** `false`
- **Explanation:** All three values count as array elements despite being null or falsy.

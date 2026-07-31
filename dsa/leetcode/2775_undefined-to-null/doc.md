# Undefined to Null

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2775 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/undefined-to-null/) |

## Problem Description

### Goal

Given a deeply nested JavaScript object or array `obj`, replace every property or array element whose value is `undefined` with `null`, and return the resulting root value. The nesting may contain any mixture of objects and arrays.

All other values must remain unchanged, including values that are already `null`. This distinction matters when data is serialized: `JSON.stringify` handles `undefined` differently from `null`, so converting the former makes those positions explicit in JSON-compatible data.

### Function Contract

**Inputs**

- `obj`: The root object or array to transform. It is valid JSON-shaped data except that any nested value may additionally be `undefined`.

The serialized size of the input is between $2$ and $10^5$ characters. Let $n$ denote the total number of enumerable object properties and array elements visited across the nested structure.

For the app-local serializable adapter, `value` contains the JSON-safe part of the input and each path in `undefinedPaths` identifies a location to materialize as JavaScript `undefined`. Benchmarks may use a `wideUndefined` object plan instead of listing every property and path.

**Return value**

Return the root object or array after every nested `undefined` value has become `null`. Existing `null` values and every other value are preserved.

### Examples

**Example 1**

- Input: `obj = {"a": undefined, "b": 3}`
- Output: `{"a": null, "b": 3}`
- Explanation: Only the value at key `"a"` changes.

**Example 2**

- Input: `obj = {"a": undefined, "b": ["a", undefined]}`
- Output: `{"a": null, "b": ["a", null]}`
- Explanation: The traversal converts values in both objects and nested arrays.

**Example 3**

- Input: `obj = [null, {"ready": false, "value": undefined}]`
- Output: `[null, {"ready": false, "value": null}]`
- Explanation: The existing `null` and boolean stay unchanged.

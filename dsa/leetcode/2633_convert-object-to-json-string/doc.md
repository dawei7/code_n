# Convert Object to JSON String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2633 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-object-to-json-string/) |

## Problem Description

### Goal

Given a valid JSON value, construct and return its JSON text representation without calling the built-in `JSON.stringify` method. The input may be a string, number, boolean, `null`, array, or object, and arrays and objects may contain any of those value types recursively.

The returned text must be valid compact JSON: do not insert spaces beyond characters that belong to string values. When serializing an object, emit its properties in the same order produced by `Object.keys(object)`. All input strings contain only alphanumeric characters, so no escape sequences are needed for their contents.

### Function Contract

**Inputs**

- `object`: A valid JSON value whose serialized representation has length from $1$ through $10^5$ and whose maximum nesting depth is at most $1000$.

Let $S$ be the number of characters in the required JSON string and $d$ the maximum array/object nesting depth.

For the app-local serializable adapter, `value` supplies the JSON value directly. A benchmark may instead use a `zeroArray` value plan to construct a legal array without storing a large repeated fixture.

**Return value**

Return the compact JSON string for `object`, preserving array order and `Object.keys` property order. Do not use `JSON.stringify` to produce it.

### Examples

#### Example 1

- **Input:** `object = {"y":1,"x":2}`
- **Output:** `{"y":1,"x":2}`
- **Explanation:** The output keeps the key order returned by `Object.keys(object)`.

#### Example 2

- **Input:** `object = {"a":"str","b":-12,"c":true,"d":null}`
- **Output:** `{"a":"str","b":-12,"c":true,"d":null}`
- **Explanation:** Strings, numbers, booleans, and `null` use their JSON primitive forms.

#### Example 3

- **Input:** `object = {"key":{"a":1,"b":[{},null,"Hello"]}}`
- **Output:** `{"key":{"a":1,"b":[{},null,"Hello"]}}`
- **Explanation:** Recursive serialization handles objects and arrays nested inside one another.

#### Example 4

- **Input:** `object = true`
- **Output:** `true`
- **Explanation:** A primitive value is itself a complete JSON value.

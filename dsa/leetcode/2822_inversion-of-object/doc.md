# Inversion of Object

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2822 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/inversion-of-object/) |

## Problem Description

### Goal

Given a JavaScript object or array `obj`, create a new object that exchanges every property key with its string value. When `obj` is an array, treat its indices as the original keys.

If a value occurs once, the inverted object maps that value directly to the corresponding key. If several original keys share the same value, map that value to an array containing all of those keys in their JavaScript enumeration order. Every input value is a string.

### Function Contract

**Inputs**

- `obj`: A valid JSON object or array whose property values are strings. Its serialized length is between $2$ and $10^5$ characters.

Let $n$ be the number of enumerable entries in `obj`.

**Return value**

Return a new object. For every distinct input value $v$:

- if exactly one key has value $v$, the output property `v` contains that key as a string;
- if several keys have value $v$, the output property `v` contains their key strings in enumeration order.

Array indices therefore appear as strings such as `"0"` and `"1"`.

### Examples

**Example 1**

For `{"a":"1","b":"2","c":"3","d":"4"}`, every value is unique. The result is `{"1":"a","2":"b","3":"c","4":"d"}`.

**Example 2**

For `{"a":"1","b":"2","c":"2","d":"4"}`, the value `"2"` occurs under both `"b"` and `"c"`. The result is `{"1":"a","2":["b","c"],"4":"d"}`.

**Example 3**

For the array `["1","2","3","4"]`, the original keys are its indices. The result is `{"1":"0","2":"1","3":"2","4":"3"}`.

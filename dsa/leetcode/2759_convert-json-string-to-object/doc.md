# Convert JSON String to Object

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2759 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Convert JSON String to Object](https://leetcode.com/problems/convert-json-string-to-object/) |

## Problem Description

### Goal

Given a valid JSON string `str`, reconstruct and return the JavaScript value that it represents without calling the built-in `JSON.parse` method.

The input may describe an object, an array, a string, a number, a boolean, or `null`. Objects and arrays may contain any of those JSON value types recursively. String contents do not contain escape sequences, and the input contains no invisible characters; punctuation such as commas may still appear inside a quoted string and must not be mistaken for structural syntax.

### Function Contract

**Inputs**

- `str`: A valid JSON string with length $1 \leq \lvert\texttt{str}\rvert \leq 10^5$.

**Return value**

Return the parsed JavaScript value: `null`, a boolean, a number, a string, an array, or an object. The parser must not use `JSON.parse`.

### Examples

**Example 1**

- Input: `str = '{"a":2,"b":[1,2,3]}'`
- Output: `{"a":2,"b":[1,2,3]}`
- Explanation: The outer value is an object whose second property contains an array.

**Example 2**

- Input: `str = 'true'`
- Output: `true`
- Explanation: A JSON document may consist of a primitive value.

**Example 3**

- Input: `str = '[1,5,"false",{"a":2}]'`
- Output: `[1,5,"false",{"a":2}]`
- Explanation: The quoted `"false"` is a string, while the remaining entries retain their own JSON types.

# Mini Parser

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 385 |
| Difficulty | Medium |
| Topics | String, Stack, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/mini-parser/) |

## Problem Description
### Goal
Given a valid serialized value, parse either one signed integer or a recursively nested list enclosed by square brackets. List elements are comma-separated and may themselves be integers, empty lists, or further nested lists.

Return the complete represented hierarchy without losing list boundaries, sign information, value order, or duplicate occurrences. A top-level standalone integer must remain an integer rather than an unnecessary one-element list. The app uses ordinary Python lists and integers, while the native implementation must construct the equivalent `NestedInteger` objects. Consume the entire input, including nested closing brackets, rather than stopping after the first parsed value.

### Function Contract
**Inputs**

- `s`: a valid serialization containing integers, square brackets, commas, and optional minus signs

**Return value**

- The app adapter returns the equivalent structure using Python integers and lists. Native LeetCode returns the corresponding `NestedInteger` object.

### Examples
**Example 1**

- Input: `s = "324"`
- Output: `324`

**Example 2**

- Input: `s = "[123,[456,[789]]]"`
- Output: `[123,[456,[789]]]`

**Example 3**

- Input: `s = "[-1,[],[2,-30]]"`
- Output: `[-1,[],[2,-30]]`

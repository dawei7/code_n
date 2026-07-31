# Deep Merge of Two Objects

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2755 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/deep-merge-of-two-objects/) |

## Problem Description

### Goal

Given two arbitrary JSON values `obj1` and `obj2`, construct their deep merge. Each input may be `null`, a boolean, a number, a string, an array, or an object.

When both current values are plain objects, include every key appearing in either one. A key found in only one input retains that input's value. For a shared key, recursively merge its two associated values.

When both current values are arrays, apply the same rule with array indices as keys. The result therefore has the length of the longer array: shared positions merge recursively, while a position present in only one array remains unchanged.

For every other pair—including primitives, `null`, or an array paired with an object—the second value replaces the first. Both inputs are valid outputs of `JSON.parse`, and each serialized input has length from 1 through $5 \cdot 10^5$.

### Function Contract

Let $n$ and $m$ denote the numbers of JSON nodes and container entries in `obj1` and `obj2`, respectively.

**Inputs**

- `obj1`: The first valid JSON value.
- `obj2`: The second valid JSON value.

Each value's serialized length is at most $5 \cdot 10^5$ characters.

**Return value**

Return the recursively merged JSON value. Matching objects combine keys, matching arrays combine indices, and every incompatible or non-container pair resolves to `obj2`.

### Examples

**Example 1**

- Input: `obj1 = {"a":1,"c":3}, obj2 = {"a":2,"b":2}`
- Output: `{"a":2,"c":3,"b":2}`
- Explanation: The shared primitive at `a` comes from the second object, while both unique keys remain.

**Example 2**

- Input: `obj1 = [{},2,3], obj2 = [[],5]`
- Output: `[[],5,3]`
- Explanation: Object and array values at index 0 are incompatible, index 1 is replaced, and the first array's trailing value remains.

**Example 3**

- Input: `obj1 = true, obj2 = null`
- Output: `null`
- Explanation: The roots are not two compatible containers, so the second value is the result.

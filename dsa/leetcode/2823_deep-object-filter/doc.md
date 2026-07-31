# Deep Object Filter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2823 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/deep-object-filter/) |

## Problem Description

### Goal

Given a JSON object or array `obj` and a Boolean predicate `fn`, filter the structure at every nesting level.

Apply `fn` to primitive leaf values. Remove every leaf for which the predicate returns `false`. After filtering descendants, also remove any object or array that has become empty. Arrays must be compacted so retained elements remain in their original relative order without holes; retained object properties keep their original keys.

If no value remains anywhere in the root object or array, return `undefined`.

### Function Contract

**Inputs**

- `obj`: A valid JSON object or array. Its serialized length is between $2$ and $10^5$ characters.
- `fn`: A function that accepts a primitive leaf value and returns a Boolean.

Let $V$ be the total number of enumerable entries visited across every object and array, and let $D$ be the maximum nesting depth.

**Return value**

Return a newly filtered object or array with all rejected leaves and newly empty containers removed. Return `undefined` when the filtered root has no remaining entries. Do not mutate `obj`.

### Examples

**Example 1**

Filtering `[-5,-4,-3,-2,-1,0,1]` with `x => x > 0` leaves `[1]`.

**Example 2**

Filtering `{"a":1,"b":"2","c":3,"d":"4","e":5,"f":6,"g":{"a":1}}` for string leaves removes all numeric leaves. The nested object under `g` becomes empty and is pruned, producing `{"b":"2","d":"4"}`.

**Example 3**

Filtering `[-1,[-1,-1,5,-1,10],-1,[-1],[-5]]` for positive leaves gives `[[5,10]]`. The two nested arrays with no surviving elements are removed.

**Example 4**

For `[[[[5]]]]` with `x => Array.isArray(x)`, the predicate is evaluated only on the numeric leaf. Nothing survives, so the result is `undefined`.

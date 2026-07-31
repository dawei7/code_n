# Join Two Arrays by ID

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2722 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Open problem](https://leetcode.com/problems/join-two-arrays-by-id/) |

## Problem Description

### Goal

Two valid JSON arrays, `arr1` and `arr2`, contain objects with integer `id` properties. Within either individual array, every `id` is unique. Form a new array containing exactly one object for every distinct identifier appearing in either input.

If an identifier occurs in only one array, preserve that object. If it occurs in both, shallowly merge their properties: keep keys found in only one object, and for any key shared by both objects, use the value from `arr2`. Nested objects and arrays are property values and are replaced as whole values rather than merged recursively. Return the joined objects in ascending order by `id`.

### Function Contract

Let $N=\lvert\texttt{arr1}\rvert+\lvert\texttt{arr2}\rvert$ and let $U$ be the number of distinct identifiers.

**Inputs**

- `arr1`: A valid JSON array whose objects have unique integer `id` values within this array.
- `arr2`: Another valid JSON array with the same per-array uniqueness guarantee. Its property values take precedence when an `id` occurs in both inputs.

The serialized length of each input array is between $2$ and $10^6$ characters.

**Return value**

Return $U$ shallowly joined objects sorted by `id` in ascending order. Every identifier appears exactly once.

### Examples

**Example 1**

- Input: `arr1 = [{"id":1,"x":1},{"id":2,"x":9}], arr2 = [{"id":3,"x":5}]`
- Output: `[{"id":1,"x":1},{"id":2,"x":9},{"id":3,"x":5}]`
- Explanation: No identifier overlaps, so the objects only need ordering.

**Example 2**

- Input: Objects with `id = 2` occur in both arrays and carry different `x` and `y` values.
- Output: The joined `id = 2` object uses both values from `arr2`.
- Explanation: Properties from the second array override matching properties from the first.

**Example 3**

- Input: Both `id = 1` objects contain nested property `b` and array property `v`, while only `arr1` contains `y`.
- Output: `b` and `v` are replaced by the values from `arr2`, while `y` remains.
- Explanation: The merge is shallow, so nested values are not recursively combined.

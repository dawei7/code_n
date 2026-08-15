# Array Prototype Last

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2619 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/array-prototype-last/) |

## Problem Description

### Goal

Extend JavaScript's `Array` prototype with a method named `last` so that the method is available on every array. Calling `array.last()` must return the array's final element without removing or otherwise changing any element.

If the receiver is empty, return the number `-1` instead. The array may be assumed to be a valid result of `JSON.parse`, so its elements can be any JSON values, including `null`, booleans, numbers, strings, nested arrays, and objects. The array length is between $0$ and $1000$, inclusive.

### Function Contract

**Inputs**

- `nums`: The JSON-compatible array that receives the `last` method through `Array.prototype`.

**Return value**

Return the element at the final array index when `nums` is non-empty; otherwise return `-1`. The method must not mutate `nums`.

### Examples

#### Example 1

- **Input:** `nums = [null, {}, 3]`
- **Output:** `3`
- **Explanation:** The final element is the number `3`.

#### Example 2

- **Input:** `nums = []`
- **Output:** `-1`
- **Explanation:** The designated result for an empty array is `-1`.

#### Example 3

- **Input:** `nums = [1, 2, -1]`
- **Output:** `-1`
- **Explanation:** Here `-1` is an actual final element; the same value also serves as the empty-array sentinel.

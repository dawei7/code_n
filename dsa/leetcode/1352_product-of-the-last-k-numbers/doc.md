# Product of the Last K Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1352 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Design, Data Stream, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/product-of-the-last-k-numbers/) |

## Problem Description

### Goal

Design a `ProductOfNumbers` data structure for a stream of nonnegative integers. Calling `add(num)` appends `num` to the stream. Calling `getProduct(k)` must return the product of the last `k` appended numbers; every query guarantees that at least `k` numbers have been added.

The operation sequence can contain zeroes. Any queried suffix containing a zero has product zero, while queries confined to numbers added after the most recent zero must return their exact product. Support a long interleaving of additions and queries without recomputing each suffix from scratch.

### Function Contract

**Inputs**

- `add(num)`: append one nonnegative integer to the stream.
- `getProduct(k)`: request the product of the last $k$ appended values.
- The app-local `solve(operations)` adapter receives `[method, arguments]` pairs.
- Let $q$ be the total number of operations.

**Return value**

- `add` returns no value.
- `getProduct(k)` returns the exact integer product of the requested suffix.
- The app-local adapter returns every method result in order, using `null` for additions.

### Examples

**Example 1**

- Operations: add `3, 0, 2, 5, 4`; query the last `2`, `3`, and `4` values; add `8`; query the last `2`.
- Output: `[null, null, null, null, null, 20, 40, 0, null, 32]`

**Example 2**

- Operations: add `1, 2, 3`; query the last `3`.
- Output: `[null, null, null, 6]`

**Example 3**

- Operations: add `0, 9`; query the last `1` and `2`.
- Output: `[null, null, 9, 0]`

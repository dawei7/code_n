# Product of the Last K Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1352 |
| Difficulty | Medium |
| Topics | Array, Math, Design, Data Stream, Prefix Sum |
| Official Link | [product-of-the-last-k-numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/) |

## Problem Description & Examples
### Goal
Design a stream structure that appends numbers and returns the product of the last `k` appended numbers.

### Function Contract
**Inputs**

- `add(num)`: appends `num` to the stream.
- `getProduct(k)`: asks for the product of the latest `k` numbers.

**Return value**

`getProduct(k)` returns the requested product.

### Examples
**Example 1**

- Input: `add(3); add(0); add(2); add(5); add(4); getProduct(2); getProduct(3); getProduct(4); add(8); getProduct(2)`
- Output: `20, 40, 0, 32`

**Example 2**

- Input: `add(1); add(2); add(3); getProduct(3)`
- Output: `6`

**Example 3**

- Input: `add(0); add(9); getProduct(1); getProduct(2)`
- Output: `9, 0`

---

## Underlying Base Algorithm(s)
Prefix products with zero reset.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per operation.
- **Space Complexity**: `O(n)` for values since the most recent zero.

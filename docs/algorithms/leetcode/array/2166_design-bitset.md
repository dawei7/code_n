# Design Bitset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2166 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Design |
| Official Link | [design-bitset](https://leetcode.com/problems/design-bitset/) |

## Problem Description & Examples
### Goal
Design a fixed-size bitset supporting individual set and clear operations, a global flip, checks for whether all or any bits are set, a count of set bits, and conversion to its binary string representation.

### Function Contract
**Inputs**

- `size`: the number of bits, initially all zero.
- Operations may supply `idx`, a zero-based bit index, for `fix(idx)` or `unfix(idx)`.

**Return value**

Mutating operations return nothing. `all()` and `one()` return booleans, `count()` returns the number of logical `1` bits, and `toString()` returns all bits from index `0` through `size - 1`.

### Examples
**Example 1**

- Input: `size = 5`; operations: `fix(3)`, `fix(1)`, `toString()`, `count()`
- Output: `"01010"`, then `2`

**Example 2**

- Input: `size = 3`; operations: `fix(0)`, `flip()`, `toString()`, `all()`, `one()`
- Output: `"011"`, then `false`, then `true`

**Example 3**

- Input: `size = 2`; operations: `fix(0)`, `fix(1)`, `unfix(0)`, `count()`, `toString()`
- Output: `1`, then `"01"`

---

## Underlying Base Algorithm(s)
Store physical bits, a boolean indicating whether their logical meaning is globally flipped, and the logical count of ones. `fix` and `unfix` compare the requested logical value with the physical value under the flip flag and update only when needed. `flip` toggles the flag and changes the count to `size - count`, making the operation constant time.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per operation except `toString()`, which is `O(size)`
- **Space Complexity**: `O(size)`

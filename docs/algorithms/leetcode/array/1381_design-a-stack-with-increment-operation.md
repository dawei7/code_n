# Design a Stack With Increment Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1381 |
| Difficulty | Medium |
| Topics | Array, Stack, Design |
| Official Link | [design-a-stack-with-increment-operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) |

## Problem Description & Examples
### Goal
Design a bounded stack that supports pushing, popping, and incrementing the bottom `k` stored values by a given amount.

### Function Contract
**Inputs**

- Constructor: `maxSize`, the stack capacity.
- `push(x)`: adds `x` if capacity allows.
- `pop()`: removes and returns the top value, or returns `-1` when empty.
- `increment(k, val)`: adds `val` to the bottom `k` elements, or all elements if fewer than `k` exist.

**Return value**

Methods mutate stack state; `pop` returns the removed value or `-1`.

### Examples
**Example 1**

- Input: `CustomStack(2); push(1); push(2); pop()`
- Output: `2`

**Example 2**

- Input: `CustomStack(3); push(1); push(2); increment(2, 5); pop()`
- Output: `7`

**Example 3**

- Input: `CustomStack(1); pop()`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Array-backed stack. The direct approach updates the bottom `min(k, size)` entries during `increment`; an optimized lazy approach stores pending increments by depth and pushes them downward when popping.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` for `push` and `pop`; `O(k)` per direct `increment`, or `O(1)` with lazy increments.
- **Space Complexity**: `O(maxSize)`

# Next Greater Element I

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `stack_02` |
| Frontend ID | 496 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Stack, Monotonic Stack |
| Official Link | [next-greater-element-i](https://leetcode.com/problems/next-greater-element-i/) |

## Problem Description & Examples
### Goal
For each index i, return the next value to the right that's
strictly greater than arr[i], or -1 if none. Monotonic stack
of indices: pop while arr[i] > arr[top], record arr[i] as the
answer for the popped index.
Requirement: O(n) time.
Source: https://www.geeksforgeeks.org/next-greater-element/

### Function Contract
**Inputs**

- `arr`: list of n random integers.
- `n`: length of arr.

**Return value**

a list of n values (each the next greater to the right, or -1).

### Examples
_This local spec has fewer than three authored examples. Add original examples before marking this reference complete._

---

## Underlying Base Algorithm(s)
stack

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `TODO`

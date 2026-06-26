# K Divisible Elements Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2261 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Trie, Rolling Hash, Hash Function, Enumeration |
| Official Link | [k-divisible-elements-subarrays](https://leetcode.com/problems/k-divisible-elements-subarrays/) |

## Problem Description & Examples
### Goal
Count distinct nonempty subarrays containing at most `k` elements divisible by `p`. Subarrays are distinct by value sequence, not by their positions.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: the maximum number of divisible elements.
- `p`: the divisor.

**Return value**

The number of distinct qualifying subarray value sequences.

### Examples
**Example 1**

- Input: `nums = [2, 3, 3, 2, 2]`, `k = 2`, `p = 2`
- Output: `11`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`, `k = 1`, `p = 4`
- Output: `10`

**Example 3**

- Input: `nums = [2, 2]`, `k = 0`, `p = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
Start a subarray at every index and extend it rightward while counting values divisible by `p`. Stop that start when the count exceeds `k`; otherwise insert the current value sequence into a set. A trie or collision-safe rolling representation can avoid repeatedly copying complete tuples, but the same bounded enumeration principle applies.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` extensions, with additional representation cost if full tuples are copied
- **Space Complexity**: `O(n^2)` in the worst case for distinct subarrays

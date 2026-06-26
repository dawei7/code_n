# Count Triplets That Can Form Two Arrays of Equal XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1442 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Bit Manipulation, Prefix Sum |
| Official Link | [count-triplets-that-can-form-two-arrays-of-equal-xor](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) |

## Problem Description & Examples
### Goal
Count triples `(i, j, k)` with `i < j <= k` where the XOR of `arr[i..j-1]` equals the XOR of `arr[j..k]`.

### Function Contract
**Inputs**

- `arr`: a list of integers.

**Return value**

The number of valid triples.

### Examples
**Example 1**

- Input: `arr = [2,3,1,6,7]`
- Output: `4`

**Example 2**

- Input: `arr = [1,1,1,1,1]`
- Output: `10`

**Example 3**

- Input: `arr = [2,3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Prefix XOR counting. If two prefix XOR values at positions `a` and `b` are equal, every split between them creates a valid triple, contributing `b - a - 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

# Check If Array Pairs Are Divisible by k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1497 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [check-if-array-pairs-are-divisible-by-k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) |

## Problem Description & Examples
### Goal
Decide whether the array can be partitioned into pairs whose sums are all divisible by `k`.

### Function Contract
**Inputs**

- `arr`: a list of integers.
- `k`: the divisor.

**Return value**

`true` if such a pairing exists, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5,10,6,7,8,9], k = 5`
- Output: `true`

**Example 2**

- Input: `arr = [1,2,3,4,5,6], k = 7`
- Output: `true`

**Example 3**

- Input: `arr = [1,2,3,4,5,6], k = 10`
- Output: `false`

---

## Underlying Base Algorithm(s)
Remainder counting. Remainder `0` values must pair among themselves, and every remainder `r` must have the same count as remainder `k - r`; when `k` is even, remainder `k/2` must also have even count.

---

## Complexity Analysis
- **Time Complexity**: `O(n + k)`
- **Space Complexity**: `O(k)`

# Check If All 1's Are at Least Length K Places Away

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1437 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [check-if-all-1s-are-at-least-length-k-places-away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) |

## Problem Description & Examples
### Goal
Check whether every pair of `1` bits in the binary array has at least `k` zeroes between them.

### Function Contract
**Inputs**

- `nums`: a binary array.
- `k`: the required minimum number of zeroes between consecutive `1`s.

**Return value**

`true` if all `1`s are sufficiently separated, otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1,0,0,0,1,0,0,1], k = 2`
- Output: `true`

**Example 2**

- Input: `nums = [1,0,0,1,0,1], k = 2`
- Output: `false`

**Example 3**

- Input: `nums = [0,1,0,0,1], k = 1`
- Output: `true`

---

## Underlying Base Algorithm(s)
Track the index of the previous `1`. When another `1` is found, the index gap must be greater than `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

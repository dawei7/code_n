# Count Good Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1534 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [count-good-triplets](https://leetcode.com/problems/count-good-triplets/) |

## Problem Description & Examples
### Goal
Count index triples `i < j < k` whose three pairwise absolute differences
satisfy the given limits `a`, `b`, and `c`.

### Function Contract
**Inputs**

- `arr`: an integer array.
- `a`: maximum allowed `abs(arr[i] - arr[j])`.
- `b`: maximum allowed `abs(arr[j] - arr[k])`.
- `c`: maximum allowed `abs(arr[i] - arr[k])`.

**Return value**

The number of good triplets.

### Examples
**Example 1**

- Input: `arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3`
- Output: `4`

**Example 2**

- Input: `arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1`
- Output: `0`

**Example 3**

- Input: `arr = [1, 2, 3], a = 1, b = 1, c = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
The straightforward solution enumerates all triples `i < j < k` and checks the
three constraints directly. The constraints are small enough for this cubic
scan.

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)`.
- **Space Complexity**: `O(1)`.

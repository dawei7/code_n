# Count Good Meals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1711 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [count-good-meals](https://leetcode.com/problems/count-good-meals/) |

## Problem Description & Examples
### Goal
Count pairs of meals whose deliciousness values sum to a power of two. Return the count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `deliciousness`: a list of non-negative integers.

**Return value**

Return the number of index pairs `(i, j)` with `i < j` and `deliciousness[i] + deliciousness[j]` equal to a power of two.

### Examples
**Example 1**

- Input: `deliciousness = [1,3,5,7,9]`
- Output: `4`

**Example 2**

- Input: `deliciousness = [1,1,1,3,3,3,7]`
- Output: `15`

**Example 3**

- Input: `deliciousness = [0,0,1,1]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Scan values while maintaining a frequency map of previously seen values. For each current value, test every relevant power of two and add the count of its complement. Then record the current value. The power range is bounded by the largest possible pair sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n * B)`, where `B` is the number of powers checked
- **Space Complexity**: `O(n)`

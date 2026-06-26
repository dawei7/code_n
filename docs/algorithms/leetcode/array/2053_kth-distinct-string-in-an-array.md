# Kth Distinct String in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2053 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [kth-distinct-string-in-an-array](https://leetcode.com/problems/kth-distinct-string-in-an-array/) |

## Problem Description & Examples
### Goal
Find the `k`th string that appears exactly once, preserving the original array order.

### Function Contract
**Inputs**

- `arr`: a list of strings.
- `k`: one-based rank among distinct strings.

**Return value**

Return the `k`th distinct string, or `""` if fewer than `k` exist.

### Examples
**Example 1**

- Input: `arr = ["d","b","c","b","c","a"], k = 2`
- Output: `"a"`

**Example 2**

- Input: `arr = ["aaa","aa","a"], k = 1`
- Output: `"aaa"`

**Example 3**

- Input: `arr = ["a","b","a"], k = 3`
- Output: `""`

---

## Underlying Base Algorithm(s)
Count all strings, then scan the array again. Decrement `k` for each string whose count is one; the string that makes `k` zero is the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

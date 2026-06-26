# Check If String Is a Prefix of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1961 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, String |
| Official Link | [check-if-string-is-a-prefix-of-array](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/) |

## Problem Description & Examples
### Goal
Check whether a target string is exactly formed by concatenating some non-empty prefix of the given word array.

### Function Contract
**Inputs**

- `s`: the target string.
- `words`: a list of strings.

**Return value**

Return `True` if `s` equals `words[0] + ... + words[i]` for some `i`, otherwise `False`.

### Examples
**Example 1**

- Input: `s = "iloveleetcode", words = ["i","love","leetcode","apples"]`
- Output: `True`

**Example 2**

- Input: `s = "iloveleetcode", words = ["apples","i","love","leetcode"]`
- Output: `False`

**Example 3**

- Input: `s = "abc", words = ["ab","c"]`
- Output: `True`

---

## Underlying Base Algorithm(s)
Concatenate words from the front until the built string reaches or exceeds the target length, then compare with `s`. A pointer-based scan can avoid building a large temporary string.

---

## Complexity Analysis
- **Time Complexity**: `O(len(s) + total checked word length)`
- **Space Complexity**: `O(1)` with pointer comparison.

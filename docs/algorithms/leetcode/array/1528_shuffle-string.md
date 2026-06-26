# Shuffle String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1528 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [shuffle-string](https://leetcode.com/problems/shuffle-string/) |

## Problem Description & Examples
### Goal
Rearrange the characters of `s` so that the character originally at index `i`
moves to index `indices[i]`.

### Function Contract
**Inputs**

- `s`: the original string.
- `indices`: a permutation of positions in `s`.

**Return value**

The restored string after placing each character at its target index.

### Examples
**Example 1**

- Input: `s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3]`
- Output: `"leetcode"`

**Example 2**

- Input: `s = "abc", indices = [0, 1, 2]`
- Output: `"abc"`

**Example 3**

- Input: `s = "aiohn", indices = [3, 1, 4, 2, 0]`
- Output: `"nihao"`

---

## Underlying Base Algorithm(s)
Allocate a character array of the same length as `s`, then for each original
index place `s[i]` into `result[indices[i]]`. Join the result array at the end.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

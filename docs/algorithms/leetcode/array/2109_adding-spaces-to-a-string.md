# Adding Spaces to a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2109 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, String, Simulation |
| Official Link | [adding-spaces-to-a-string](https://leetcode.com/problems/adding-spaces-to-a-string/) |

## Problem Description & Examples
### Goal
Insert spaces before specified character indices in a string.

### Function Contract
**Inputs**

- `s`: source string.
- `spaces`: sorted insertion indices.

**Return value**

Return the string after all spaces are inserted.

### Examples
**Example 1**

- Input: `s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]`
- Output: `"Leetcode Helps Me Learn"`

**Example 2**

- Input: `s = "icodeinpython", spaces = [1,5,7,9]`
- Output: `"i code in py thon"`

**Example 3**

- Input: `s = "spacing", spaces = [0,1,2,3,4,5,6]`
- Output: `" s p a c i n g"`

---

## Underlying Base Algorithm(s)
Walk through `s` and the sorted `spaces` list together. Before appending character `s[i]`, append a space when `i` is the next insertion index.

---

## Complexity Analysis
- **Time Complexity**: `O(len(s) + len(spaces))`
- **Space Complexity**: `O(len(s) + len(spaces))` for the result.

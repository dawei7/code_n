# Maximum Length of a Concatenated String with Unique Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1239 |
| Difficulty | Medium |
| Topics | Array, String, Backtracking, Bit Manipulation |
| Official Link | [maximum-length-of-a-concatenated-string-with-unique-characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) |

## Problem Description & Examples
### Goal
Pick any subsequence of strings, concatenate them in order, and maximize the length of a result that contains no repeated character.

### Function Contract
**Inputs**

- `arr`: list of lowercase strings.

**Return value**

The maximum possible length of a concatenation whose characters are all unique.

### Examples
**Example 1**

- Input: `arr = ["un","iq","ue"]`
- Output: `4`

**Example 2**

- Input: `arr = ["cha","r","act","ers"]`
- Output: `6`

**Example 3**

- Input: `arr = ["abcdefghijklmnopqrstuvwxyz"]`
- Output: `26`

---

## Underlying Base Algorithm(s)
Bitmask backtracking / dynamic set expansion.

---

## Complexity Analysis
- **Time Complexity**: `O(2^n)` in the number of usable strings.
- **Space Complexity**: `O(2^n)` for the set of reachable masks.

# Find Common Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1002 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [find-common-characters](https://leetcode.com/problems/find-common-characters/) |

## Problem Description & Examples
### Goal
Given a list of lowercase words, return all characters that appear in every word. If a character appears multiple times in every word, include it that many times in the result.

### Function Contract
**Inputs**

- `words`: List[str]

**Return value**

List[str] - common characters with multiplicity

### Examples
**Example 1**

- Input: `words = ["bella", "label", "roller"]`
- Output: `["e", "l", "l"]`

**Example 2**

- Input: `words = ["cool", "lock", "cook"]`
- Output: `["c", "o"]`

**Example 3**

- Input: `words = ["abc", "def"]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Frequency-count intersection.

---

## Complexity Analysis
- **Time Complexity**: `O(total characters)`
- **Space Complexity**: `O(1)` for the fixed lowercase alphabet

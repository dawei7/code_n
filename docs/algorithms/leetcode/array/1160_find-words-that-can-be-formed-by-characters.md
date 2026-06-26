# Find Words That Can Be Formed by Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1160 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [find-words-that-can-be-formed-by-characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) |

## Problem Description & Examples
### Goal
Given a pool of characters, add up the lengths of all words that can be built using each pool character at most once per word.

### Function Contract
**Inputs**

- `words`: list of lowercase words.
- `chars`: available lowercase characters.

**Return value**

The total length of all buildable words.

### Examples
**Example 1**

- Input: `words = ["cat","bt","hat","tree"]`, `chars = "atach"`
- Output: `6`

**Example 2**

- Input: `words = ["hello","world","leetcode"]`, `chars = "welldonehoneyr"`
- Output: `10`

**Example 3**

- Input: `words = ["a","aa","aaa"]`, `chars = "aa"`
- Output: `3`

---

## Underlying Base Algorithm(s)
Frequency counting.

---

## Complexity Analysis
- **Time Complexity**: `O(total characters in words + len(chars))`
- **Space Complexity**: `O(1)` for the lowercase alphabet counts.

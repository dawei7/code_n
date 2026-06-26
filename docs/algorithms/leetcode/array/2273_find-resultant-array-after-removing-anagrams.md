# Find Resultant Array After Removing Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2273 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [find-resultant-array-after-removing-anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |

## Problem Description & Examples
### Goal
Repeatedly remove a word when it is an anagram of the word immediately before it. Return the stable remaining sequence.

### Function Contract
**Inputs**

- `words`: a list of lowercase words.

**Return value**

The words left after all adjacent anagram removals, preserving order.

### Examples
**Example 1**

- Input: `words = ["abba", "baba", "bbaa", "cd", "cd"]`
- Output: `["abba", "cd"]`

**Example 2**

- Input: `words = ["a", "b", "c", "d", "e"]`
- Output: `["a", "b", "c", "d", "e"]`

**Example 3**

- Input: `words = ["abc", "cba", "bac"]`
- Output: `["abc"]`

---

## Underlying Base Algorithm(s)
Compute a canonical signature for each word, such as its sorted characters or 26-letter frequency tuple. Keep the first word, then retain each later word only when its signature differs from the last retained signature. Removed words never change the signature of their surviving predecessor.

---

## Complexity Analysis
- **Time Complexity**: `O(L log A)` with per-word sorting, where `L` is total characters and `A` bounds word length
- **Space Complexity**: `O(L)` for the output and signatures

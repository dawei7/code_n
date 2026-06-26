# Count Words Obtained After Adding a Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2135 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Bit Manipulation, Sorting |
| Official Link | [count-words-obtained-after-adding-a-letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/) |

## Problem Description & Examples
### Goal
Count target words that can be formed by taking a start word, adding one letter not already present in it, and rearranging the letters. Letters within every given word are distinct.

### Function Contract
**Inputs**

- `startWords`: the available lowercase source words.
- `targetWords`: the lowercase words to test.

**Return value**

The number of target words obtainable by the permitted operation.

### Examples
**Example 1**

- Input: `startWords = ["ant", "act", "tack"]`, `targetWords = ["tack", "act", "acti"]`
- Output: `2`

**Example 2**

- Input: `startWords = ["ab", "a"]`, `targetWords = ["abc", "abcd"]`
- Output: `1`

**Example 3**

- Input: `startWords = ["g", "xy"]`, `targetWords = ["gh", "xyz"]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Represent each word as a 26-bit letter mask and store all start-word masks in a set. For each target mask, remove each one of its letters in turn; the target is obtainable if any resulting mask belongs to the start set. The distinct-letter guarantee makes the mask representation exact.

---

## Complexity Analysis
- **Time Complexity**: `O(L)`, where `L` is the total number of characters across all words
- **Space Complexity**: `O(S)`, where `S` is the number of distinct start-word masks

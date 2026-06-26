# String Matching in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1408 |
| Difficulty | Easy |
| Topics | Array, String, String Matching |
| Official Link | [string-matching-in-an-array](https://leetcode.com/problems/string-matching-in-an-array/) |

## Problem Description & Examples
### Goal
Return every word that appears as a substring inside another word from the same list.

### Function Contract
**Inputs**

- `words`: a list of distinct strings.

**Return value**

A list of words that are substrings of at least one different word in `words`.

### Examples
**Example 1**

- Input: `words = ["mass","as","hero","superhero"]`
- Output: `["as","hero"]`

**Example 2**

- Input: `words = ["leetcode","et","code"]`
- Output: `["et","code"]`

**Example 3**

- Input: `words = ["blue","green","red"]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Pairwise substring checking. Compare each word with every other word and include it once when it is found inside a longer candidate.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 * L^2)` in a straightforward substring-search model, where `L` is the maximum word length.
- **Space Complexity**: `O(1)` besides the output.

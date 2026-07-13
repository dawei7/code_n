# Before and After Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1181 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [before-and-after-puzzle](https://leetcode.com/problems/before-and-after-puzzle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/before-and-after-puzzle/).

### Goal
Combine two different phrases when the last word of the first phrase equals the first word of the second phrase. The overlapping word appears only once in the merged phrase. Return all unique merged phrases in lexicographic order.

### Function Contract
**Inputs**

- `phrases`: List of phrases containing lowercase words separated by single spaces.

**Return value**

Sorted list of unique before-and-after puzzles.

### Examples
**Example 1**

- Input: `phrases = ["writing code", "code rocks"]`
- Output: `["writing code rocks"]`

**Example 2**

- Input: `phrases = ["a b", "b c", "a b c"]`
- Output: `["a b c"]`

**Example 3**

- Input: `phrases = ["a", "a"]`
- Output: `["a"]`

---

## Solution
### Approach
Precompute each phrase's first word and last word. Map first words to the phrase indices that start with that word.

For each phrase as the "before" part, look up phrases whose first word equals its last word. For every different index, merge the before phrase with the after phrase excluding its first word. Store results in a set, then return them sorted.

### Complexity Analysis
- **Time Complexity**: `O(total_words + r log r)`, plus the cost of constructing `r` generated phrases.
- **Space Complexity**: `O(total_words + r)`, where `r` is the number of unique generated puzzles.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

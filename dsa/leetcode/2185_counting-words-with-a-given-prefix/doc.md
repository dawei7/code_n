# Counting Words With a Given Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2185 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [counting-words-with-a-given-prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/counting-words-with-a-given-prefix/).

### Goal
Count how many words begin with a specified prefix.

### Function Contract
**Inputs**

- `words`: a list of lowercase words.
- `pref`: the lowercase prefix to match.

**Return value**

The number of words whose first characters equal `pref`.

### Examples
**Example 1**

- Input: `words = ["pay", "attention", "practice", "attend"]`, `pref = "at"`
- Output: `2`

**Example 2**

- Input: `words = ["leetcode", "win", "loops", "success"]`, `pref = "code"`
- Output: `0`

**Example 3**

- Input: `words = ["a", "aa", "ab"]`, `pref = "a"`
- Output: `3`

---

## Solution
### Approach
Scan the list and use a prefix comparison for each word, incrementing the result whenever the word starts with `pref`.

### Complexity Analysis
- **Time Complexity**: `O(W * P)` in the worst case, where `W` is the number of words and `P` is the prefix length
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

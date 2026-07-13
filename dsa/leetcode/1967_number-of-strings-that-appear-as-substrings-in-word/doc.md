# Number of Strings That Appear as Substrings in Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1967 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-strings-that-appear-as-substrings-in-word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/).

### Goal
Count how many pattern strings appear somewhere inside a given word.

### Function Contract
**Inputs**

- `patterns`: candidate strings.
- `word`: the string to search within.

**Return value**

Return the number of pattern entries that are substrings of `word`.

### Examples
**Example 1**

- Input: `patterns = ["a","abc","bc","d"], word = "abc"`
- Output: `3`

**Example 2**

- Input: `patterns = ["a","b","c"], word = "aaaaabbbbb"`
- Output: `2`

**Example 3**

- Input: `patterns = ["a","a","a"], word = "ab"`
- Output: `3`

---

## Solution
### Approach
For the small direct version, test each pattern with substring search against `word` and count successful pattern entries. A trie or automaton is only needed for much larger constraints.

### Complexity Analysis
- **Time Complexity**: `O(p * |word|)` in the simple approach.
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

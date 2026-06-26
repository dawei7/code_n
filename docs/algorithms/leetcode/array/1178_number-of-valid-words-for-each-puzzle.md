# Number of Valid Words for Each Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1178 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Bit Manipulation, Trie |
| Official Link | [number-of-valid-words-for-each-puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) |

## Problem Description & Examples
### Goal
For each seven-letter puzzle, count words that use only letters from that puzzle and contain the puzzle's first letter.

### Function Contract
**Inputs**

- `words`: list of lowercase words.
- `puzzles`: list of seven-letter lowercase puzzle strings.

**Return value**

For each puzzle, the number of valid words.

### Examples
**Example 1**

- Input: `words = ["aaaa","asas","able","ability","actt","actor","access"]`, `puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]`
- Output: `[1,1,3,2,4,0]`

**Example 2**

- Input: `words = ["apple","pleas","please"]`, `puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]`
- Output: `[0,1,3,2,0]`

**Example 3**

- Input: `words = ["abc","abd","bcd"]`, `puzzles = ["abcdefg","bcdefga"]`
- Output: `[2,3]`

---

## Underlying Base Algorithm(s)
Bitmask frequency counting and submask enumeration.

---

## Complexity Analysis
- **Time Complexity**: `O(total_word_letters + puzzles * 2^6)`
- **Space Complexity**: `O(number of distinct word masks)`

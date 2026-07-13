# Check if Word Can Be Placed In Crossword

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2018 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-word-can-be-placed-in-crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/).

### Goal
Determine whether a word can be placed into a crossword slot horizontally or vertically, either forward or backward, matching existing letters and using only blank cells.

### Function Contract
**Inputs**

- `board`: a grid containing letters, spaces, and blocker `'#'`.
- `word`: the word to place.

**Return value**

Return `True` if the word fits in any valid slot, otherwise `False`.

### Examples
**Example 1**

- Input: `board = [["#"," ","#"],[" "," ","#"],["#","c"," "]], word = "abc"`
- Output: `True`

**Example 2**

- Input: `board = [[" ","#","a"],[" ","#","c"],[" ","#","a"]], word = "ac"`
- Output: `False`

**Example 3**

- Input: `board = [["#"," ","#"],[" "," ","#"],["#"," ","c"]], word = "ca"`
- Output: `True`

---

## Solution
### Approach
Extract every maximal non-blocked segment from rows and columns. A segment is usable only if its length equals the word length and every occupied letter matches either the word or the reversed word at that position.

### Complexity Analysis
- **Time Complexity**: `O(mn * L)` in a straightforward segment check.
- **Space Complexity**: `O(1)` excluding temporary segment traversal.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

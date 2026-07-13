# Alphabet Board Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1138 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [alphabet-board-path](https://leetcode.com/problems/alphabet-board-path/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/alphabet-board-path/).

### Goal
On an alphabet board containing `a` through `z`, produce a sequence of moves that visits and selects each character in `target`. Moves are `U`, `D`, `L`, `R`, and `!` selects the current character.

### Function Contract
**Inputs**

- `target`: String to spell on the board.

**Return value**

Move string that spells `target`.

### Examples
**Example 1**

- Input: `target = "leet"`
- Output: `"DDR!UURRR!!DDD!"`

**Example 2**

- Input: `target = "code"`
- Output: `"RR!DDRR!UUL!R!"`

**Example 3**

- Input: `target = "az"`
- Output: `"!DDDDD!"`

---

## Solution
### Approach
Map every character to its board row and column. For each target character, move from the current position to the target position, then append `!`.

The special cell `z` is alone in its row, so moving left and up before moving down and right avoids stepping into invalid cells. A safe order is: move `U`, then `L`, then `D`, then `R`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `target`.
- **Space Complexity**: `O(n)` for the output string.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

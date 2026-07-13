# Rotating the Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1861 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [rotating-the-box](https://leetcode.com/problems/rotating-the-box/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/rotating-the-box/).

### Goal
Rotate a box 90 degrees clockwise after stones fall as far right as possible within each row, stopping at obstacles.

### Function Contract
**Inputs**

- `box`: a grid containing stones `#`, obstacles `*`, and empty cells `.`.

**Return value**

Return the rotated box after gravity has affected the stones.

### Examples
**Example 1**

- Input: `box = [["#",".","#"]]`
- Output: `[["."],["#"],["#"]]`

**Example 2**

- Input: `box = [["#",".","*","."],["#","#","*","."]]`
- Output: `[["#","."],["#","#"],["*","*"],[".","."]]`

**Example 3**

- Input: `box = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]`
- Output: `[[".","#","#"],[".","#","#"],["#","#","*"],["#","*","."],["#",".","*"],["#",".","."]]`

---

## Solution
### Approach
Process each row from right to left with a write pointer for the next position where a stone can fall. Obstacles reset the write pointer to the cell before them. Move stones to the write pointer and leave empties behind. After all rows settle, rotate the matrix clockwise.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for the rotated result

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._

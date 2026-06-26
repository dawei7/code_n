## Problem Description & Examples
### Goal
Given an `m x n` grid of characters `board` and a string `word`, return `True` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Function Contract
**Inputs**

- `board`: List[List[str]]
- `word`: str

**Return value**

bool - True if word exists

### Examples
**Example 1**

- Input: `board = [["A", "B"], ["C", "D"]], word = "ACD"`
- Output: `True`

**Example 2**

- Input: `board = [['E', 'E'], ['A', 'C']], word = 'EECA'`
- Output: `True`

**Example 3**

- Input: `board = [['B', 'F'], ['A', 'C']], word = 'AB'`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

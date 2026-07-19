# Baseball Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 682 |
| Difficulty | Easy |
| Topics | Array, Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/baseball-game/) |

## Problem Description
### Goal
You are keeping a baseball game's scores under unusual rules, beginning with an empty record. Process each string in `operations` in order: an integer records that score, `+` records the sum of the previous two valid scores, `D` records double the previous valid score, and `C` invalidates and removes the previous valid score.

Return the sum of all scores remaining in the record after every operation. Removed scores no longer count and are also ignored by later `+` and `D` operations. The input guarantees that each operation has enough preceding valid scores when its rule requires them.

### Function Contract
**Inputs**

- `operations`: a valid sequence of integer strings and the commands `+`, `D`, and `C`

**Return value**

- The total of all scores that remain valid after every operation is processed

### Examples
**Example 1**

- Input: `operations = ["5","2","C","D","+"]`
- Output: `30`

**Example 2**

- Input: `operations = ["5","-2","4","C","D","9","+","+"]`
- Output: `27`

**Example 3**

- Input: `operations = ["1","C"]`
- Output: `0`

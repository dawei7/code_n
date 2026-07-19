# Zuma Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 488 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Stack, Breadth-First Search, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/zuma-game/) |

## Problem Description
### Goal
You have one row of colored balls on the board and a small collection of balls in your hand. On each turn, choose one hand ball and insert it between two board balls or at either end. Whenever three or more consecutive balls of one color form a group, that group is removed; the resulting neighbors may form another removable group, and this reaction continues until the row is stable.

Return the minimum number of inserted balls needed to remove every ball from the board, or `-1` when it is impossible to clear the row with the available hand. Each hand occurrence may be used at most once, insertion order matters, and clearing a group can be useful because it joins formerly separated colors for a later chain reaction.

### Function Contract
**Inputs**

- `board`: the current row using `R`, `Y`, `B`, `G`, and `W`
- `hand`: the available multiset of balls encoded with the same letters

**Return value**

- The minimum number of insertions needed to empty the board, or `-1`

### Examples
**Example 1**

- Input: `board = "WRRBBW", hand = "RB"`
- Output: `-1`

**Example 2**

- Input: `board = "WWRRBBWW", hand = "WRBRW"`
- Output: `2`

**Example 3**

- Input: `board = "G", hand = "GGGGG"`
- Output: `2`

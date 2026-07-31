# Determine the Winner of a Bowling Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2660 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/) |

## Problem Description

### Goal

Two 0-indexed arrays `player1` and `player2` record how many of ten pins each player hits during the same $n$ turns. Ordinarily a turn contributes its recorded pin count. However, if that player hit all `10` pins in either of the preceding two turns, the current turn contributes twice its recorded count.

Compute both players' total scores under this rule. Return `1` when player 1 has the larger score, `2` when player 2 has the larger score, and `0` when their scores are equal. A strike affects only later turns, never its own value unless an earlier strike also applies.

### Function Contract

**Inputs**

- `player1`: Player 1's pin counts for $n$ turns.
- `player2`: Player 2's pin counts for the same $n$ turns, where $1 \le n \le 1000$ and every count is between `0` and `10` inclusive.

**Return value**

- Return `1` for a player 1 win, `2` for a player 2 win, or `0` for a draw.

### Examples

**Example 1**

- Input: `player1 = [5,10,3,2], player2 = [6,5,7,3]`
- Output: `1`
- Explanation: Player 1 scores `25` because the final two turns are doubled; player 2 scores `21`.

**Example 2**

- Input: `player1 = [3,5,7,6], player2 = [8,10,10,2]`
- Output: `2`
- Explanation: Player 2's strikes make the later eligible turns worth twice their pin counts.

**Example 3**

- Input: `player1 = [2,3], player2 = [4,1]`
- Output: `0`
- Explanation: Both players score `5`.

**Example 4**

- Input: `player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]`
- Output: `2`
- Explanation: The respective totals are `73` and `75`.

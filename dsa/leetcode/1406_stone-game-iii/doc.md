# Stone Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1406 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/stone-game-iii/) |

## Problem Description

### Goal

Stones are arranged in a row, and `stoneValue[i]` is the possibly negative value of one stone. Alice and Bob alternate turns, with Alice moving first. On a turn, the player removes the first one, two, or three remaining stones and adds their values to their score.

The game ends after every stone has been taken. Both players choose moves optimally. Return `"Alice"` when Alice's final score is greater, `"Bob"` when Bob's is greater, and `"Tie"` when the scores are equal.

### Function Contract

**Inputs**

- `stoneValue`: an array of $n$ integers, where $1 \le n \le 5 \times 10^4$ and $-1000 \le \texttt{stoneValue[i]} \le 1000$.

**Return value**

- `"Alice"`, `"Bob"`, or `"Tie"` according to optimal play and final scores.

### Examples

**Example 1**

- Input: `stoneValue = [1,2,3,7]`
- Output: `"Bob"`

**Example 2**

- Input: `stoneValue = [1,2,3,-9]`
- Output: `"Alice"`

**Example 3**

- Input: `stoneValue = [1,2,3,6]`
- Output: `"Tie"`

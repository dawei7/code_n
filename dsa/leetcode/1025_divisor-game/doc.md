# Divisor Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1025 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/divisor-game/) |

## Problem Description

### Goal

Alice and Bob play a turn-based game, with Alice moving first. The chalkboard initially contains the positive integer `n`.

On a turn, the current player must choose an integer `x` such that $0 < x < n$ and `n % x == 0`, then replace the chalkboard number with `n - x`. A player who has no valid move loses.

Return `true` if and only if Alice wins when both players choose their moves optimally.

### Function Contract

**Inputs**

- `n`: the initial chalkboard number, where $1 \le n \le 1000$.

**Return value**

- `true` exactly when Alice can force a win; otherwise, `false`.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `true`
- Explanation: Alice subtracts `1`, leaving `1`; Bob then has no valid move.

**Example 2**

- Input: `n = 3`
- Output: `false`
- Explanation: Alice's only move subtracts `1`. Bob does the same from `2`, leaving Alice unable to move from `1`.

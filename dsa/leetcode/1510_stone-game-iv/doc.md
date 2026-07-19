# Stone Game IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1510 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-iv/) |

## Problem Description
### Goal

Alice and Bob play a turn-based game on one pile containing $n$ stones, with Alice moving first. On each turn, the current player must remove a non-zero square number of stones: $1,4,9,16,\ldots$, provided that many stones remain.

A player who has no legal move loses. Given the positive initial pile size, determine whether Alice can force a win when both players choose their moves optimally.

### Function Contract
**Inputs**

- `n`: The initial number of stones, satisfying $1 \leq n \leq 10^5$.
- A legal move from a pile of size $s$ removes $k^2$ stones for some positive integer $k$ with $k^2 \leq s$.
- Both players know the full game state and play optimally; there is no randomness or hidden information.

**Return value**

Return `True` exactly when Alice has a strategy that wins from the initial state `n`; otherwise return `False`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `True`
- Explanation: Alice removes the one stone, leaving Bob with no move.

**Example 2**

- Input: `n = 2`
- Output: `False`
- Explanation: The only move leaves one stone, which Bob removes.

**Example 3**

- Input: `n = 4`
- Output: `True`
- Explanation: Alice removes all four stones in one square-number move.

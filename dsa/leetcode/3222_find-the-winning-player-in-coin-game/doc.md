# Find the Winning Player in Coin Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3222 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-winning-player-in-coin-game/) |

## Problem Description

### Goal

There are `x` coins worth `75` each and `y` coins worth `10` each. Alice and Bob alternate turns, with Alice moving first. On every turn, the current player must remove coins whose combined value is exactly `115`.

A player who cannot form that total loses immediately. Both players know the remaining counts and play optimally. Return `"Alice"` or `"Bob"` according to which player wins. Removed coins do not return to the game, and a turn must use whole coins from the two available denominations.

### Function Contract

**Inputs**

- `x`: The number of `75`-value coins, with $1 \leq x \leq 100$.
- `y`: The number of `10`-value coins, with $1 \leq y \leq 100$.

**Return value**

Return the winning player's name, either `"Alice"` or `"Bob"`.

### Examples

#### Example 1

- **Input:** `x = 2, y = 7`
- **Output:** `"Alice"`
- **Explanation:** Alice removes one `75` coin and four `10` coins, after which Bob cannot move.

#### Example 2

- **Input:** `x = 4, y = 11`
- **Output:** `"Bob"`
- **Explanation:** Exactly two turns are possible, so Alice moves first and Bob moves last.

#### Example 3

- **Input:** `x = 1, y = 1`
- **Output:** `"Bob"`
- **Explanation:** Alice cannot total `115` on the first turn.

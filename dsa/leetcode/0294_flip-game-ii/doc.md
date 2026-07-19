# Flip Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 294 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Backtracking, Memoization, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-game-ii/) |

## Problem Description
### Goal
Two players alternate turns on a string containing only `+` and `-`. A legal move changes one adjacent `"++"` pair into `"--"`, permanently removing that pair as plus signs. The first player moves from the supplied initial state.

Assuming optimal play, return `True` when the first player can choose moves that guarantee the opponent eventually faces a state with no legal move. Return `False` when the opponent can force that outcome against every first choice, including when the initial state already has no flippable pair. The result is strategic existence, not a list of winning moves or game states.

### Function Contract
**Inputs**

- `currentState`: the initial row of plus and minus symbols

**Return value**

`True` exactly when the first player has a winning strategy.

### Examples
**Example 1**

- Input: `currentState = "++++"`
- Output: `true`

**Example 2**

- Input: `currentState = "+"`
- Output: `false`

**Example 3**

- Input: `currentState = "++"`
- Output: `true`

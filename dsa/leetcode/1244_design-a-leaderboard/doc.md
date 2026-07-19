# Design A Leaderboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1244 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-leaderboard/) |

## Problem Description

### Goal

Design a `Leaderboard` that stores each active player's accumulated score. `addScore(playerId, score)` adds `score` to the player's existing total, creating the player when no score is currently recorded. `top(K)` returns the sum of the $K$ highest active totals.

`reset(playerId)` removes that player's score from the leaderboard, after which a later `addScore` for the same identifier starts again from zero. Calls arrive in order, every reset names an active player, and every `top` request asks for no more players than are currently present.

### Function Contract

**Inputs**

- `operations`: An ordered cOde(n) trace of `[method, args]` calls for one `Leaderboard` instance.
- `addScore(playerId, score)`: Uses identifiers and positive added scores in the allowed integer ranges.
- `top(K)`: Requests the sum of the $K$ highest current scores.
- `reset(playerId)`: Removes an existing player's accumulated score.

Let $p$ be the number of active players at a `top(K)` call.

**Return value**

- The ordered call results: `null` for `addScore` and `reset`, and the requested integer sum for each `top`.

### Examples

**Example 1**

- Input: `operations = [["addScore",[1,73]],["addScore",[2,56]],["addScore",[3,39]],["addScore",[4,51]],["addScore",[5,4]],["top",[1]],["reset",[1]],["reset",[2]],["addScore",[2,51]],["top",[3]]]`
- Output: `[null,null,null,null,null,73,null,null,null,141]`

The final active top three scores are $51$, $51$, and $39$.

**Example 2**

Adding twice for one player accumulates both values before `top` is evaluated.

**Example 3**

After `reset`, adding a score for that identifier creates a fresh total rather than restoring the removed score.

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

### Required Complexity

- **Time:** $O(p\log K)$
- **Space:** $O(p)$

<details>
<summary>Approach</summary>

#### General

**Store one total per active player.** A hash map from player ID to accumulated score makes `addScore` a direct addition and `reset` a direct deletion. Resetting truly removes the entry, so a later addition naturally begins from zero.

**Select only the requested leaders.** For `top(K)`, use a size-$K$ selection heap through `nlargest` rather than sorting all scores. The heap retains the best $K$ values seen so far; summing those values gives exactly the requested total. Equal scores occupy separate heap entries because they belong to separate players.

**Replay the app operation trace.** Construct one leaderboard and invoke each method in order, appending its result. This preserves state across calls while keeping the native class interface intact beside the app-local `solve(operations)` adapter.

#### Complexity detail

`addScore` and `reset` take expected $O(1)$ time. With $p$ active players, `top(K)` examines all scores and maintains a heap of at most $K$, taking $O(p\log K)$ time. The score map plus selection heap use $O(p)$ space overall.

#### Alternatives and edge cases

- **Sort every score for each `top`:** It is correct but takes $O(p\log p)$ even when $K$ is small.
- **Repeated linear maximum selection:** Selecting one unused leader at a time takes $O(Kp)$ time.
- **Always-sorted score list:** `top` becomes fast, but every score addition or reset requires locating and updating an ordered entry.
- **Score buckets:** Bounded scores can support frequency trees, but accumulated totals and implementation complexity make a heap selection simpler here.
- **Repeated addition:** Add to the current total rather than replacing it.
- **Tied scores:** Each tied active player counts separately toward $K$.
- **Reset then add:** The new total contains only scores added after the reset.

</details>

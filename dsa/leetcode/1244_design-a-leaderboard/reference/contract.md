## Function Contract

**Native interface**

- `Leaderboard()`: Constructs an empty leaderboard.
- `addScore(playerId, score)`: Mutates the leaderboard and returns no value.
- `top(K)`: Returns the integer sum of the $K$ greatest active scores without changing the leaderboard.
- `reset(playerId)`: Removes an active player's accumulated score and returns no value.

Authored cOde(n) cases encode calls after construction as ordered `[method, arguments]` pairs in `operations`. That trace is an app fixture for invoking the source-native class, not an additional LeetCode method.

Let $p$ be the number of active players when `top(K)` is called. Tied scores belong to distinct players and therefore occupy distinct positions among the top $K$ values.

**Return value**

For the app trace, return results in call order: `null` for each mutating operation and the requested score sum for each `top` call.

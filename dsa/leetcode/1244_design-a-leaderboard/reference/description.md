## Description

Design a Leaderboard class, which has 3 functions:

- `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.

- `top(K)`: Return the score sum of the top `K` players.

- `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.
### Function Contract

**Native interface**

- `Leaderboard()`: Constructs an empty leaderboard.
- `addScore(playerId, score)`: Mutates the leaderboard and returns no value.
- `top(K)`: Returns the integer sum of the $K$ greatest active scores without changing the leaderboard.
- `reset(playerId)`: Removes an active player's accumulated score and returns no value.

Authored cOde(n) cases encode calls after construction as ordered `[method, arguments]` pairs in `operations`. That trace is an app fixture for invoking the source-native class, not an additional LeetCode method.

Let $p$ be the number of active players when `top(K)` is called. Tied scores belong to distinct players and therefore occupy distinct positions among the top $K$ values.

**Return value**

For the app trace, return results in call order: `null` for each mutating operation and the requested score sum for each `top` call.

### Examples

#### Example 1

- **Input:** ``
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
- **Output:** ``
[null,null,null,null,null,null,73,null,null,null,141]
- **Explanation:**
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
### Constraints

- $1 \le playerId, K \le 10000$

- It's guaranteed that `K` is less than or equal to the current number of players.

- $1 \le score \le 100$

- There will be at most `1000` function calls.
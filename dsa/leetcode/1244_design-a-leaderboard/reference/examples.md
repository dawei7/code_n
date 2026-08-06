## Examples

**Example 1**

- Input: `commands = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"], arguments = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]`
- Output: `[null,null,null,null,null,null,73,null,null,null,141]`
- Explanation: The trace proceeds as follows.

1. Construct an empty `Leaderboard`.
2. `addScore(1, 73)` leaves the active entries as `[[1,73]]`.
3. `addScore(2, 56)` produces `[[1,73],[2,56]]`.
4. `addScore(3, 39)` produces `[[1,73],[2,56],[3,39]]`.
5. `addScore(4, 51)` produces `[[1,73],[2,56],[3,39],[4,51]]`.
6. `addScore(5, 4)` produces `[[1,73],[2,56],[3,39],[4,51],[5,4]]`.
7. `top(1)` returns `73`.
8. `reset(1)` removes player `1`, leaving players `2`, `3`, `4`, and `5`.
9. `reset(2)` then leaves players `3`, `4`, and `5`.
10. `addScore(2, 51)` creates player `2` again with the fresh score `51`.
11. `top(3)` returns `141`, the sum `51 + 51 + 39`.

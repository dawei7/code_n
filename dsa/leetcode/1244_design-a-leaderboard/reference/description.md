## Description

Design a `Leaderboard` class that begins empty and supports three operations:

- `addScore(playerId, score)` adds `score` to that player's current total. If the identifier is not active, create it with the supplied score.
- `top(K)` returns the sum of the $K$ highest current player totals.
- `reset(playerId)` sets the named player's score back to zero by removing that player from the leaderboard. The player is guaranteed to be active when this operation is called.

Operations arrive in order and share one leaderboard instance, so additions accumulate until a reset removes that player's state.

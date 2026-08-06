## Description

The `Matches` table records the matches played by each player. A row identifies
the player, the match date, and whether that match ended in a `Win`, `Draw`, or
`Lose`. The pair `(player_id, match_day)` is unique, so a player's matches have
an unambiguous chronological order.

A winning streak is a sequence of consecutive matches by the same player whose
results are all `Win`. Either a draw or a loss ends the current streak; gaps
between match dates do not. Return every player represented in `Matches`
together with the greatest number of consecutive wins in that player's
history. A player who has never won must still appear with a longest streak of
zero. The result rows may be returned in any order.

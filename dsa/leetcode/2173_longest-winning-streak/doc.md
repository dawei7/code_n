# Longest Winning Streak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2173 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-winning-streak/) |

## Problem Description

### Goal

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

### Function Contract

**Inputs**

`Matches` contains:

- `player_id`: the integer identifier of the player.
- `match_day`: the date on which that player played the match.
- `result`: one of `Win`, `Draw`, or `Lose`.

The composite key `(player_id, match_day)` is unique.

**Return value**

Return a table with columns `player_id` and `longest_streak`. It must contain
one row for every distinct player in `Matches`, and `longest_streak` must be
that player's maximum chronological run of `Win` results, or `0` when no such
match exists.

### Examples

#### Example 1

- **Input:** player `1` records `Win, Win, Win, Draw, Win`; player `2` records
  `Lose, Lose`; and player `3` records one `Win`.
- **Output:** `(1, 3)`, `(2, 0)`, and `(3, 1)`.

#### Example 2

- **Input:** one player's chronological results are `Win, Draw, Win, Win, Lose,
  Win`.
- **Output:** that player's `longest_streak` is `2`.

#### Example 3

- **Input:** a player wins on two non-adjacent calendar dates and has no match
  between them.
- **Output:** that player's `longest_streak` is `2`, because only intervening match
  results—not idle calendar days—break a streak.

# Find Players With Zero or One Losses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2225 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-players-with-zero-or-one-losses/) |

## Problem Description

### Goal

Each pair `[winner, loser]` records the outcome of one match between two different players. Match outcomes are unique, although a player may participate in many matches as a winner, loser, or both.

Return two groups considering only players who participated in at least one recorded match. The first group contains every player with no losses, and the second contains every player with exactly one loss. Values in each group must appear in increasing order; players with two or more losses belong to neither group.

### Function Contract

**Inputs**

- `matches`: A nonempty list of unique `[winner, loser]` pairs with different positive player identifiers.

Let $m=\lvert\texttt{matches}\rvert$ and let $p$ be the number of distinct participating players.

**Return value**

Return `[zero_loss_players, one_loss_players]`, with both inner lists sorted in increasing order.

### Examples

#### Example 1

- **Input:** `matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]`
- **Output:** `[[1, 2, 10], [4, 5, 7, 8]]`

#### Example 2

- **Input:** `matches = [[2, 3], [1, 3], [5, 4], [6, 4]]`
- **Output:** `[[1, 2, 5, 6], []]`

#### Example 3

- **Input:** `matches = [[1, 2]]`
- **Output:** `[[1], [2]]`

## General

**Maintain both player identity and sorted score order**

The three operations need two different views of the same active players:

- `addScore` and `reset` must find a player by `playerId`.
- `top(K)` must access the greatest scores in sorted order.

One data structure is not ideal for both jobs, so the exact class keeps them synchronized:

- `self.d` maps every active player ID to that player’s current accumulated score.
- `self.rank` is a `SortedList` containing one score entry per active player, in nondecreasing order.

Tied scores appear multiple times in `self.rank` because different players still occupy different leaderboard positions.

**Class invariant**

After every mutating call:

1. the keys of `self.d` are exactly the active players;
2. `self.d[playerId]` is that player’s current score;
3. the multiset of values in `self.d` is exactly the multiset stored in `self.rank`.

All operation reasoning follows from preserving this invariant.

**Adding a new player**

If `playerId not in self.d`, the player has no active accumulated score. The code stores the supplied `score` in the dictionary and inserts that same value into the sorted list.

Both representations gain exactly one matching entry, so the invariant holds.

Although `self.d` is a `defaultdict(int)`, the source checks membership before reading a missing player. It therefore does not rely on automatic zero insertion for this operation.

**Updating an existing player**

An existing player’s old score is already represented once in `self.rank`. The source removes one occurrence of `self.d[playerId]`, adds the new points to the dictionary value, and inserts the updated total.

Removal must happen before changing the dictionary, because the old score is the value that must disappear from the sorted multiset.

If several players share that score, `SortedList.remove` deletes one equal occurrence. That is exactly right: only this player is changing, while the other tied players remain.

For example, if players A and B both have 51 and A gains 10, one 51 is removed and 61 is inserted. The other 51 remains for B.

**Returning the top \(K\) total**

`self.rank` is ascending, so its last \(K\) entries are the greatest \(K\) player scores. The slice `self.rank[-K:]` obtains those entries, and `sum` returns their total.

The contract guarantees \(K\) does not exceed the active player count. No special handling for an undersized leaderboard is necessary.

This operation does not mutate either data structure.

**Resetting a player**

`self.d.pop(playerId)` removes the active dictionary entry and returns its score. The exact code passes that returned score to `self.rank.remove`, deleting one matching multiset occurrence.

The contract guarantees the player is active, so `pop` and `remove` both succeed. Afterward, neither representation contains that player’s contribution.

Reset means removal rather than retaining a zero-score player. A later `addScore` for the same ID follows the new-player branch, as the example demonstrates.

**Following the example**

After adding scores 73, 56, 39, 51, and 4, the sorted list is `[4,39,51,56,73]`. `top(1)` takes the final element and returns 73.

Resetting players 1 and 2 removes 73 and 56 from both representations. Adding player 2 with 51 now treats that ID as new. The scores are 39, 51, 51, and 4, sorted as `[4,39,51,51]`. The last three sum to 141.

**Why both structures are necessary**

A dictionary alone supports updates well but would require selecting or sorting scores for every top query. A sorted list alone makes top queries convenient but cannot identify which score to remove when a specific player updates. The dictionary supplies the old value, and the sorted multiset maintains rank order.


Construction creates two empty representations, satisfying the invariant. Each add branch inserts one matching dictionary and sorted entry, while an update replaces exactly one old multiset value with the matching new dictionary value. Reset removes the same active score from both.

By induction, the sorted list always contains exactly all active scores. Its final \(K\) elements are therefore exactly the top \(K\) player scores, including separate tied players, and their sum is correct.

**Required support library**

`SortedList` is supplied by the `sortedcontainers` package rather than Python’s standard library. A standalone environment must import and install that dependency, and must import `defaultdict` from `collections`.

## Complexity detail

Let \(p\) be the number of active players.

Dictionary membership, lookup, update, and pop are expected \(O(1)\). `SortedList.add` and `remove` are documented as approximately \(O(\log p)\) search plus block-maintenance costs, conventionally treated as \(O(\log p)\). Thus `addScore` and `reset` are \(O(\log p)\).

`top(K)` locates and slices the final range, then sums \(K\) values, for roughly \(O(\log p+K)\) time and \(O(K)\) temporary slice space. The manifest’s \(O(p\log K)\) describes scanning all players with a size-\(K\) heap, not this maintained sorted-list source.

The dictionary and sorted list each store \(p\) entries, so persistent space is \(O(p)\).

## Alternatives and edge cases

- **Dictionary plus size-\(K\) heap per query:** Updates are expected \(O(1)\), while `top(K)` costs \(O(p\log K)\), matching the manifest but repeating selection work.
- **Dictionary plus sort per query:** Simple, but each top call costs \(O(p\log p)\).
- **Score-frequency ordered map:** Store how many players have each score and traverse scores descending. It can reduce duplicated keys but needs an ordered-map implementation.
- **Tied scores:** `SortedList` stores duplicate values, so every tied player is counted separately.
- **Update an existing player:** The old score must be removed before the new total is inserted.
- **Reset then add again:** Reset erases the ID; a later score starts a new accumulation.
- **Guaranteed valid \(K\):** Negative slicing returns exactly \(K\) values because enough active players exist.
- **Guaranteed active reset:** The exact code raises if asked to reset an absent player, but such a call is outside the contract.
- **External dependency:** `SortedList` is not built into Python and must be available in the execution environment.
- **Input calls capped:** The source remains efficient across mixed operations without rebuilding the complete ranking.

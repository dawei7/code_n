## General

**Expose the useful ordering.** Sort player abilities and trainer capacities. The smallest unmatched player is the easiest remaining player to serve. A trainer below that ability cannot serve this player or any later, stronger player, so discarding that trainer is always safe.

**Use the smallest sufficient trainer.** Scan trainers from smallest to largest. Whenever the current capacity reaches the smallest unmatched player's ability, pair them and advance to the next player. Giving that player a larger trainer cannot improve the count: exchanging the chosen trainer with the smallest sufficient one preserves every possible later assignment while keeping larger capacities available.

Every trainer is considered once after sorting, and the player pointer advances exactly once per match. When the scan ends, no unused trainer can serve the smallest still-unmatched player, so no additional valid pair exists.

## Complexity detail

Sorting costs $O(n\log n + m\log m)$ time, followed by an $O(n+m)$ scan. Python's sorting implementation may use $O(n+m)$ auxiliary space; the pointer scan itself uses $O(1)$.

## Alternatives and edge cases

- **Repeated best-trainer search:** For each player, scanning all unused trainers can reproduce the greedy choice but costs $O(nm)$ time.
- **Maximum-first greedy:** Matching strongest players and trainers can also be made correct, but it needs equally careful handling of trainers that are too weak.
- **Exact equality:** A trainer whose capacity equals a player's ability is valid.
- **Unequal group sizes:** The answer cannot exceed the smaller array length.
- **No feasible pair:** Trainers weaker than the smallest player are skipped, and the result may be zero.
- **Duplicate values:** Equal abilities and capacities represent distinct people and resources, so each occurrence can support one match.

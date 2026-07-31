## General

**Give every participant a loss count**

Use a hash map keyed by player identifier. When reading a match, ensure the winner exists with count zero and increment the loser's count. This records players who appear only as winners as well as every loss.

**Filter before sorting**

After all matches, collect identifiers whose counts are zero and those whose counts are one. Players with larger counts are deliberately omitted. Sort each selected group independently to meet the output contract.

Every recorded loss increments exactly one loser's counter, so the final map value equals that player's total losses. Every participant is inserted from at least one side of a match. Filtering counts zero and one therefore selects exactly the required players, and sorting changes only their prescribed order.

## Complexity detail

Let $m$ be the match count and $p$ the distinct participant count. Expected hash-map processing takes $O(m)$ time. Sorting the selected identifiers costs at most $O(p\log p)$, for $O(m+p\log p)$ total time.

The loss map and output candidates use $O(p)$ space.

## Alternatives and edge cases

- **Rescan matches per player:** Counting a player's losses by scanning all matches can take $O(mp)$ time.
- **Fixed identifier array:** The bounded player IDs permit direct counting and an ordered scan, but this depends on the numeric limit and visits unused identifiers.
- **Separate participant and loser sets:** Maintaining both works, though a zero-initialized loss map stores the same information in one structure.
- **Winner later loses:** A player remains in the map and moves out of the zero-loss group automatically.
- **Multiple losses:** Counts above one exclude the player from both result groups.
- **Disconnected matches:** Every participating component contributes independently.
- **Increasing order:** The two group positions are fixed, and each group's identifiers must be explicitly sorted.

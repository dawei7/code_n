## General

Only whether a position is occupied matters in the requested output; the number of marbles at that position never affects a later operation, because every move transfers the entire group. Represent the current occupied positions with a hash set initialized from `nums`.

For each paired source and destination, remove the source from the set and insert the destination. This also handles a destination that is already occupied, because inserting it again changes nothing. When source and destination are equal, removing and immediately reinserting the same coordinate preserves the state. After all moves, sort the set to produce the required order.

Before each operation, the set equals exactly the occupied positions after the preceding operations. Removing the guaranteed-occupied source clears precisely the position whose marbles leave, and inserting the destination marks precisely where that group arrives. Thus the invariant holds after every move, and the final sorted set is exactly the requested result.

## Complexity detail

Let $n$ be the number of initial marbles, $m$ the number of moves, and $k$ the number of final occupied positions. Building the set takes $O(n)$ expected time, the moves take $O(m)$ expected time, and sorting the result takes $O(k \log k)$ time. The total expected time is $O(n + m + k \log k)$. The occupied-position set contains at most $n$ entries, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Track every marble individually:** Rewriting every matching marble position for each move is correct but can take $O(nm)$ time.
- **Count marbles by position:** A frequency map preserves more information than necessary; counts can be merged correctly, but an occupancy set is simpler because all marbles always move together.
- **Occupied destination:** Moving onto an already occupied coordinate merges groups without creating a duplicate output position.
- **Self-move:** When source and destination are equal, the occupied set must remain unchanged.
- **Reoccupied source:** A coordinate vacated earlier may receive marbles later and then legally appear as a source again.

## General
**Tickets are edges of an Eulerian trail**

Every ticket must be used once, so the itinerary is an Eulerian trail in a directed multigraph, fixed to start at `JFK`. A simple greedy walk that permanently chooses the smallest next airport is unsafe: in the third example, choosing `KUL` immediately reaches a dead end and strands two tickets.

Hierholzer's algorithm postpones committing airports to the final route. Walk through unused edges while possible. Only when the current airport has no outgoing ticket left is it appended to the route; then backtrack to the previous airport. Reversing this dead-end order produces the complete Eulerian itinerary.

**Consume lexical choices cheaply**

Build one destination list per departure and sort each list in reverse lexical order. The smallest available destination is then at the end and can be removed in constant time. Keep an explicit stack beginning with `JFK`: if its top has an unused destination, push that destination; otherwise pop the airport into the reversed route.

Duplicate edges appear as duplicate list entries, so each ticket is naturally consumed once. An iterative stack also avoids recursion-depth failures on long itineraries.

**Postorder placement resolves necessary dead ends**

When an airport is appended, all tickets reachable from its current walk position have already been consumed, so that airport must be the end of the remaining Eulerian segment. Backtracking splices completed cycles and terminal segments into the correct trail, and every edge removal contributes exactly one transition to the final reversed route.

Choosing the smallest available edge whenever a walk advances gives the smallest lexical choice that can occupy the earliest still-unfixed route position. Edges that lead to terminal segments are placed correctly during reversal rather than invalidating the walk. Therefore Hierholzer's construction uses all tickets and produces the lexicographically smallest complete itinerary.

## Complexity detail
Let `E` be the number of tickets. Sorting all adjacency lists costs at most $O(E \log E)$. Every edge is popped once and every airport occurrence is pushed and popped once, so traversal is $O(E)$. Adjacency lists, stack, and route use $O(E)$ space.

## Alternatives and edge cases
- **Backtrack over unused tickets:** is correct but may scan or explore a combinatorial number of ticket choices.
- **Always append the smallest next destination directly to the answer:** can get trapped before all tickets are used.
- **Use a min-heap per departure:** gives the same $O(E \log E)$ bound without reverse sorting.
- Duplicate tickets must remain separate. A one-ticket input returns two airports, and lexical comparison applies to whole airport codes.

## General
**Record every city with an outgoing path.** Build a hash set containing the first city from each pair. This set describes exactly the cities from which another trip departs, independent of the order in which the pairs were supplied.

**Test destinations against that set.** Scan the second city of every pair. The destination absent from the starting-city set has no outgoing edge, so return it. The problem guarantee ensures exactly one such city exists.

**Why every other destination is excluded.** Any nonfinal destination is an intermediate city on the single chain. The next trip must start there, placing it in the set. The final city has no next trip and therefore cannot be a starting city. Thus set membership rejects all and only the intermediate destinations, leaving the unique required endpoint.

## Complexity detail
Building the set and scanning the $n$ destination entries each take $O(n)$ expected time. The set stores at most $n$ city names, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Scan all starts for every destination:** This avoids a set but repeats membership work and can take $O(n^2)$ time.
- **Follow a source-to-destination map:** Finding the initial city and walking the chain is also linear, but it maintains more structure than the endpoint question needs.
- **Rely on input order:** The paths can be shuffled, so the destination of the last array entry need not be the route endpoint.
- **Single path:** Its second city is immediately the destination.
- **City-name contents:** Compare complete strings; spaces are part of a name.
- **Uniqueness guarantee:** A disconnected graph could have several cities without outgoing edges, but the valid input is one chain with exactly one endpoint.

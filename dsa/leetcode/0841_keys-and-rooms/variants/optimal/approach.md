## General
Interpret every key `j` stored in room `i` as a directed edge from `i` to `j`. The question becomes whether all graph vertices are reachable from vertex `0`.

Mark room `0` as seen and place it on a stack. Repeatedly remove one discovered room, inspect all of its keys, and add each previously unseen destination room to both the seen set and the stack. Marking at discovery time prevents cycles, self-keys, or keys repeated across different rooms from scheduling the same room more than once.

Every processed room is reachable because it was either room `0` or was unlocked by a key in an already reachable room. Conversely, whenever a reachable room is processed, all rooms directly unlockable from it are discovered. By induction along any key path from room `0`, the traversal finds every visitable room. Therefore all rooms can be visited exactly when the seen count reaches `n`.

## Complexity detail
Each room is pushed and processed at most once, and every stored key is inspected once. The total time is $O(n+K)$. The seen structure and traversal stack contain at most $n$ room labels, giving $O(n)$ space.

## Alternatives and edge cases
- **Breadth-first search:** A queue explores the same reachable set with identical $O(n+K)$ time and $O(n)$ space.
- **Repeatedly rescan all rooms:** Looking for newly unlocked but unprocessed rooms in full passes is correct, but a chain revealed in reverse index order can require $O(n)$ scans of $n$ rooms, for $O(n^2+K)$ time.
- **Self-key:** A room containing its own key does not make that room reachable if no already reachable room unlocks it.
- **Cycles:** Rooms may unlock one another; the seen check prevents endless traversal without treating a disconnected cycle as reachable.
- **Duplicate destination across rooms:** Keys are distinct only within one room, so several rooms may unlock the same destination; it is still visited once.
- **Keys to room zero:** Such keys add no new reachability because room `0` begins unlocked.

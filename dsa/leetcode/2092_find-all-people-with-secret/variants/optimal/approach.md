## General
**Why meetings must be grouped by time**

Chronological ordering prevents a later secret from affecting an earlier meeting. Within one timestamp, however, input order has no meaning because sharing is instantaneous. All meetings at that time form an undirected temporary graph, and the secret reaches an entire connected component if any person in that component knew it before or during that timestamp.

**Finding every informed component in a batch**

Sort meetings by time and build an adjacency list for one equal-time group. Initialize a breadth-first search with the group's participants who are already in the global `informed` set. Traversal reaches exactly the temporary components seeded with the secret. Add all reached people to `informed`, discard the temporary graph, and continue to the next timestamp.

**Why temporary connectivity must not persist**

Two people who met without either knowing the secret do not remain connected for future transmission. Discarding each batch graph enforces this: only knowledge persists between timestamps. Conversely, breadth-first closure inside the batch permits an arbitrary same-time chain to transmit immediately, as required.

Every person added by the traversal is connected through meetings at the current time to someone who knew the secret, so the addition is valid. Every valid transmission chain at that time lies in such a component and is traversed, so no eligible person is missed.

## Complexity detail
Sorting $M$ meetings costs $O(M \log M)$. Each meeting contributes two temporary adjacency entries and is traversed only within its own batch, for another $O(M)$ work. Producing or maintaining the informed set costs up to $O(n)$. The total is $O(M \log M+n)$ time and $O(M+n)$ space in the largest batch.

## Alternatives and edge cases
- **Union-find with batch reset:** Union all participants at one time, keep components connected to person `0`, and reset the others; this matches the same temporal rule but requires careful rollback or parent restoration.
- **Earliest-time priority queue:** Treat each meeting as an edge usable only at or after its timestamp and compute earliest knowledge times, giving another $O(M \log n)$ approach.
- **Single pass in input order:** This can miss a same-time chain when its meetings appear in an unfavorable order.
- **Permanent union-find:** Keeping every historical meeting edge incorrectly allows a future secret to travel through an earlier uninformed meeting.
- People `0` and `firstPerson` always belong to the answer even if they attend no meetings.
- A meeting before either participant learns the secret is never revisited.
- The answer is a set semantically, so its returned order is irrelevant.

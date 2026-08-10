## General

**Process meetings in chronological groups**

Knowledge can move forward through time, never backward. The source first marks person 0 and `firstPerson` as knowing the secret, then sorts `meetings` by time.

The indices `i` and `j` identify one maximal block whose meetings all have the same timestamp. Grouping equal times is essential because sharing is instantaneous. Someone who learns the secret in one meeting at time $t$ may pass it through another meeting also at time $t$, even if that second row appears earlier or later in the input.

Processing equal-time meetings one by one would incorrectly make the input row order meaningful. Treating the entire group as a graph captures all same-time chains.

**Build a temporary graph for one timestamp**

For meetings `i` through `j`, the code builds an undirected adjacency list `g` and a participant set `s`. A meeting between `x` and `y` adds both `x -> y` and `y -> x` because either participant can share with the other.

This graph exists only for the current time. A connected component represents people linked by a chain of simultaneous meetings. If any member knew the secret before or at this time, instantaneous sharing spreads it through that entire component. A component with no knowledgeable member learns nothing.

The queue is initialized with every current participant `u` for which `vis[u]` is already true. Those are exactly the components' possible secret sources.

**Use multi-source BFS for instantaneous propagation**

The BFS removes a knowledgeable participant `u` and examines every current-time neighbor `v`. If `v` does not yet know, the code sets `vis[v] = True` and enqueues `v`.

Enqueuing newly informed people is what allows a chain such as meetings `1-2` and `2-3` at the same time to inform person 3 immediately when person 1 already knows. BFS continues until every node reachable from a knowledgeable seed in the temporary graph has been marked.

No separate local visited set is necessary. `vis` serves both as permanent knowledge and as the traversal marker. A person who already knew is included among the initial seeds, so skipping them when reached from another neighbor cannot prevent their edges from being processed.

After BFS, the temporary graph is discarded and the scan advances to the next time group. People marked in `vis` remain knowledgeable forever.

**Why isolated simultaneous components stay separate**

Two sets of meetings can share a timestamp without sharing a participant. Building one graph does not merge them; they remain different connected components.

The multi-source queue may seed one component and not another. BFS crosses only actual meeting edges, so the unseeded component remains unvisited. This matches the rule: equal time alone does not transmit a secret between people who never meet through a chain.

**Why the algorithm is correct**

Before processing a time group, assume `vis[u]` is true exactly for people who know the secret from earlier times. This is true initially for people 0 and `firstPerson` at time 0.

Within the current-time graph, a person can learn the secret exactly when their connected component contains at least one already knowledgeable person. One direction follows because a path of same-time meetings transmits the secret edge by edge instantaneously. The other follows because without such a seed, no meeting endpoint in that component begins the time knowing the secret.

Multi-source BFS visits exactly the union of components containing a seed. Marking those people therefore produces the exact knowledge state after this timestamp. Sorting ensures no later meeting influences an earlier group. By induction across all groups, the final Boolean array is correct.

The final comprehension returns every index whose flag is true. Any order is allowed, and increasing index order is a valid choice.

The source sorts `meetings` in place, so the input meeting list is left in chronological order.

## Complexity detail

Let $M$ be the number of meetings and $n$ the number of people.

Sorting costs $O(M\log M)$. Across all time groups, every meeting is inserted into one temporary graph and its two adjacency entries are examined at most once by BFS. The combined grouping and traversal work is $O(M)$, while initializing and scanning `vis` costs $O(n)$. Total time is $O(M\log M+n)$.

`vis` uses $O(n)$ space. The temporary graph, participant set, queue, and the Python group slice `meetings[i:j + 1]` can together use $O(M)$ space for the largest timestamp group. The returned list can contain $O(n)$ people. The manifest's $O(M+n)$ space bound therefore matches the exact source.

## Alternatives and edge cases

- **Process rows individually:** This can miss instantaneous chains when equal-time rows are ordered unfavorably. Equal timestamps must be handled as one connectivity event.
- **Permanent union-find:** Components formed at one time must not persist for people who never learned the secret. A temporary graph avoids leaking same-time connectivity into later times.
- **Timestamp-group union-find with reset:** DSU can union participants within one time, retain only components connected to knowledgeable people, then reset the others. It is valid but more intricate than temporary BFS.
- **Priority traversal by earliest knowledge time:** A time-aware graph search can compute earliest learning times. Sorting and grouping makes the instantaneous equivalence at each timestamp especially explicit.
- **Several known seeds in one component:** They may all enter the queue, but `vis` prevents unknown people from being enqueued repeatedly.
- **No known seed in a component:** BFS never enters it, so nobody there incorrectly learns the secret.
- **Person attends multiple meetings simultaneously:** All incident edges appear in the same temporary graph, allowing immediate receive-and-forward behavior.
- **Repeated participant across different times:** Their permanent `vis` flag seeds every later group they attend after learning.
- **People with no meetings:** Only person 0 or `firstPerson` can know without attending a meeting.
- **Input order:** Sorting deliberately mutates `meetings`; correctness depends on chronological rather than original row order.
- **Answer order:** The final enumeration is increasing, though the contract permits any ordering.

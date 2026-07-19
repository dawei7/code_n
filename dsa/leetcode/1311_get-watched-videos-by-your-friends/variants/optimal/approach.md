## General
**Use breadth-first layers to enforce shortest distance**

Begin a queue with `id` and mark that person visited. Repeat exactly `level` breadth-first expansions. During one expansion, remove every person currently in the queue and append each unvisited friend, marking on enqueue. After $k$ expansions, the queue contains exactly the people whose shortest distance from `id` is $k$.

This layer property holds because breadth-first search discovers vertices in nondecreasing shortest-path distance. Marking a person at first discovery prevents a cycle or a second path from placing the same person into a later layer. Therefore, after the requested number of expansions, neither closer people nor people first reachable farther away remain in the queue.

**Count and order only the final layer**

Accumulate a frequency map from the watched lists of people still in the queue. Sort its distinct keys by the pair `(frequency, title)`. Tuple ordering applies the required increasing count first and the alphabetical tie-break only when counts match.

## Complexity detail
Breadth-first search visits at most $n$ people and examines at most $2E$ adjacency entries, taking $O(n+E)$ time. Counting takes $O(S)$, and sorting $V$ names takes $O(V\log V)$, for $O(n+E+S+V\log V)$ total time. The visited set and queue use $O(n)$ space, while the frequency map and output use $O(V)$.

## Alternatives and edge cases
- **Depth-labeled DFS:** Recording the shortest known distance can work, but plain DFS may reach a person first by a longer path and requires extra correction; BFS represents exact shortest-distance layers directly.
- **Repeated frequency scans:** Collecting all target videos and rescanning that list once per distinct title is correct but can take $O(SV)$ time.
- **Cycles and multiple paths:** Mark people when they are enqueued so each contributes only at their shortest distance and at most once.
- **Frequency before alphabet:** A lexicographically smaller title must still come later when it has a larger count.
- **Duplicate titles for one person:** Every list occurrence contributes to the frequency; the contract counts watched-video entries, not merely viewers.
- **No person at the requested level:** The queue becomes empty and the correct result is an empty list.
- **Starting person's videos:** They are never counted because the legal target level is at least 1.

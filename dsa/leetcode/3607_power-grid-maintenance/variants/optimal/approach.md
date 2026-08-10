## General

The problem contains two kinds of state, but only one changes:

- the cables permanently determine which stations belong to the same power grid;
- stations can go offline as queries are processed.

The statement explicitly says an offline station remains part of its grid. Therefore, connectivity can be computed once at the beginning. The source uses Union-Find for those static connected components and a separate sorted collection for the currently online station IDs in each component.

**Building the permanent power grids**

The Union-Find is created with `c + 1` positions because station identifiers run from 1 through `c`. Position 0 is unused.

For every bidirectional cable `[u, v]`, `uf.union(u, v)` merges the two components. `find` uses path compression, and `union` uses component sizes to attach the smaller tree beneath the larger one. After all connections are processed:

`uf.find(x)`

is a representative for the complete static grid containing station `x`.

No later query changes the Union-Find. Taking a station offline changes who can answer maintenance checks, not which stations are directly or indirectly connected.

**One sorted online set per component**

The source creates:

`st = [SortedList() for _ in range(c + 1)]`.

Only entries whose indices are actual final Union-Find roots receive station IDs; the other sorted lists remain empty. For each station `i`, the initialization performs:

`st[uf.find(i)].add(i)`.

Initially all stations are online, so every identifier appears exactly once in the sorted list for its grid. A `SortedList` preserves ascending order while supporting membership checks and deletion.

After initialization, the intended invariant is:

> For every final root `r`, `st[r]` contains exactly the IDs of currently online stations in that connected component, in increasing order.

This invariant directly answers both cases of a maintenance query.

**Processing a type-1 maintenance query**

For query `[1, x]`, the source first obtains `root = uf.find(x)`.

It then checks `if x in st[root]`. If true, station `x` is online. The contract says an online requested station resolves its own check even if a smaller online station exists in the same grid, so the answer must be `x`.

If `x` is absent, it is offline. When `st[root]` is nonempty, its first element `st[root][0]` is the smallest online ID in the grid because the collection is sorted. That station resolves the check.

If the sorted list is empty, the component has no operational station and the answer is `-1`.

The source appends an answer only for type-1 queries, so the returned array naturally has the requested query order and length.

**Processing a type-2 offline query**

For query `[2, x]`, the code runs:

`st[root].discard(x)`.

If `x` is online, this removes it and restores the invariant with that station absent. `discard` is deliberately safe when the value is already absent, so taking an already-offline station offline again has no additional effect and raises no error.

No separate Boolean `online` array is necessary. Membership in the component's sorted list is the complete online-status record.

**Why the root remains a valid key**

Union-Find representatives can change while unions are still being performed. The source avoids a root-key inconsistency by completing every `union` before creating and filling `st`. Afterward, there are no more unions, so the partition and its final representatives remain stable. Path compression may shorten parent pointers, but `find` continues returning the same final representative for every member of a component.

If the algorithm tried to add stations to root-indexed containers before all connections were processed, later merges would require merging those containers as well. The chosen construction order avoids that complication.

**Following the first example**

All five stations are connected, so initialization places `[1, 2, 3, 4, 5]` in one component's `SortedList`.

- Query `[1, 3]` finds 3 in the list and returns 3, even though 1 is smaller.
- Query `[2, 1]` discards 1, leaving `[2, 3, 4, 5]`.
- Query `[1, 1]` finds 1 absent and returns the first list element, 2.
- Query `[2, 2]` leaves `[3, 4, 5]`.
- Query `[1, 2]` returns the new minimum, 3.

The answers are appended as `[3, 2, 3]`.

**Why the invariant proves correctness**

Initially, every station is online and is inserted into exactly the list keyed by its component root, so the invariant holds.

A type-1 query does not modify state. If `x` is present, returning it follows the self-resolution rule. If absent, the sorted list contains exactly all other online stations in the same grid, making its first entry the required smallest identifier; an empty list correctly means no resolver exists.

A type-2 query removes exactly the station going offline from exactly its component list. Other stations and all component memberships remain unchanged, so the invariant continues to hold. By induction over the query sequence, every appended answer is correct.

**How this differs from the local editorial**

The local editorial offers reverse query processing with a per-component minimum, or a DFS/BFS component map with lazy min-heaps. The exact Optimal source uses neither. It processes queries forward and performs direct deletion from a `SortedList`.

Direct deletion makes the state easy to understand, but it requires a nonstandard ordered-container implementation. The file as shown does not import `SortedList`. It works only if the execution environment already provides that name; in an ordinary standalone Python module, `SortedList` must be imported from `sortedcontainers` or the code raises `NameError`. The same source also relies on `List` being provided for its annotations. These environment dependencies are implementation facts, not changes to the underlying algorithm.

## Complexity detail

Let `c` be the number of stations, `m` the number of connections, and `q` the number of queries.

Union-Find initialization and all cable unions take `O((c+m)\alpha(c))` time, where `\alpha` is the inverse Ackermann function. Finding the root and adding each of the `c` station IDs to a sorted list costs at most `O(c\log c)` total under the ordered container's advertised operation bounds.

Each query performs one Union-Find `find`. A type-1 query performs ordered membership testing, and a type-2 query performs ordered discard; each is `O(\log c)` in the worst component-size bound. Reading the first element or checking the length is `O(1)`. Therefore, the faithful total time is:

$$
O\bigl((c+m)\alpha(c)+(c+q)\log c\bigr).
$$

The manifest gives `O((c+m)\alpha(c)+q+c\log c)`, treating the forward query phase as linear. That does not reflect the logarithmic membership and deletion operations of this exact `SortedList` implementation. A lazy-heap alternative can make total deletion cleanup amortized across queries, but that is a different source.

The Union-Find arrays use `O(c)` space. There are `c+1` sorted-list objects, and they collectively contain exactly `c` station IDs initially, so their total asymptotic space is `O(c)` despite many empty containers. The answer can contain up to `q` integers. Including output, space is `O(c+q)`; excluding output, auxiliary space is `O(c)`. The input connections are not copied into an adjacency list.

## Alternatives and edge cases

- **Reverse processing:** Count all offline operations, start from the final online state, and restore stations while scanning queries backward. Per-component minima can then be updated without deletions, but repeated offline operations require careful counting.
- **Lazy min-heaps:** Store all component IDs in heaps and mark stations offline separately. Pop offline minima only when needed; each station is removed from a heap at most once.
- **Balanced binary search tree:** Any ordered set supporting membership, deletion, and minimum can replace `SortedList` with the same high-level algorithm.
- **Unordered set only:** It supports status and deletion but cannot find the smallest online ID efficiently without scanning the whole component.
- **Recompute connectivity after an outage:** This is incorrect as well as expensive because an offline station remains part of the static power grid.
- **Requested station is online:** Return `x` itself, not the component minimum.
- **Requested station is offline:** Return the smallest remaining online ID in its original static component.
- **Entire component offline:** Its sorted list is empty, so the answer is `-1`.
- **Isolated online station:** Its component list contains only itself, and a type-1 query returns its ID.
- **Isolated station goes offline:** Its list becomes empty, and later maintenance checks return `-1`.
- **Repeated type-2 query:** `discard` leaves an already-absent value unchanged, making the operation idempotent.
- **Several disconnected grids:** Each final root indexes an independent sorted list, so outages in one grid cannot affect another.
- **Station ID 1 versus array index 0:** Arrays have length `c+1` to preserve one-based station identifiers; slot 0 is unused.
- **Duplicate connections:** Union-Find simply detects that endpoints are already connected; component membership remains correct.
- **Component root is not its smallest station:** This is harmless. The root is only a container key; `st[root][0]` supplies the smallest online ID.
- **All queries are outages:** The answer list remains empty because type 2 produces no output.
- **All queries are checks:** Every station remains online and resolves its own request.
- **Missing imports:** The exact file requires its environment to provide `SortedList` and `List`; standalone use must import them.
- **Input preservation:** The source mutates only Union-Find and sorted-list state. `connections` and `queries` retain their original order and contents.

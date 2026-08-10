## General

The initial shortest path is the chain

`0 -> 1 -> 2 -> ... -> n - 1`

with $n-1$ roads. A new road `u -> v` can replace the section of the current path from `u` through `v` with one edge. The special noncrossing-query guarantee makes it possible to maintain only the current shortest path and permanently remove cities that a useful shortcut bypasses.

The array `nxt` is a successor structure for that path. Initially `nxt[i] = i + 1`, so following successors from zero reproduces the original chain. The array has entries for zero through `n - 2`; the destination needs no successor. Variable `cnt` is the number of edges on the represented path and begins at `n - 1`.

When an active city is removed from the current path, its `nxt` entry is set to zero. Zero is a safe inactive sentinel for every removable positive city because valid successors always have a larger index and are therefore positive. Node zero itself is never removed from the start of the path.

For query `[u,v]`, the condition `0 < nxt[u] < v` asks two things. First, `nxt[u] > 0` means `u` is still on the maintained path. Second, `nxt[u] < v` means the current path leaves `u` for some city before `v`, so the new direct road bypasses at least one current path edge and strictly shortens the route.

If the condition holds, `i` begins at the old successor of `u`. While `i < v`, that active path city lies strictly between `u` and `v` and will be bypassed. Removing one intermediate path city reduces the number of path edges by one: a path segment that entered and later left that city is compressed when the shortcut replaces the whole segment. Thus `cnt` is decremented once per removed city.

The simultaneous assignment

`nxt[i], i = 0, nxt[i]`

first obtains the old successor as the next iteration's `i` while marking the current city inactive. This is essential; setting `nxt[i]` to zero before separately reading it would lose the remainder of the path. When `i` reaches `v`, all active cities between the endpoints have been removed, and `nxt[u] = v` installs the shortcut as the new successor edge.

For `n = 5`, the initial successors describe `0,1,2,3,4` and `cnt = 4`. Query `2 -> 4` removes active city three, decrements the count to three, and links two to four. Query `0 -> 2` removes city one and lowers the count to two. Query `0 -> 4` follows the current successors through two, removes it, and links zero to four, leaving count one.

If `u` is inactive, `nxt[u] = 0` and the query is ignored. If `u` is active but its current successor is already `v` or lies beyond `v`, the query cannot produce a shorter maintained path and is also ignored. In either case the existing `cnt` is appended.

**Why ignoring such roads is safe.** The noncrossing condition forbids endpoints in the pattern $u_1<u_2<v_1<v_2$. Therefore shortcuts are disjoint or nested; they do not partially interleave. Under this laminar structure, once a city is bypassed by the current shortest path, a later legal road starting at that inactive city cannot combine with the path to create a better route that requires restoring it. Similarly, if the current successor from active `u` already reaches at least as far as `v`, the existing path has an equal or stronger jump from that point.

This guarantee is what distinguishes the second problem from the first. Without it, two crossing shortcuts could combine in ways that make an earlier bypassed endpoint relevant, and a single successor chain would not retain enough information.

**Why `cnt` remains the shortest distance.** Initially it is the length of the only chain. For a useful query, the current path segment from `u` to `v` contains one more edge than the number of intermediate active cities removed plus the final arrival at `v`. Replacing that segment by one road reduces its length by exactly the number of removed cities, matching the decrements. Noncrossing ensures no alternative combination outside the maintained path is shorter. By induction after every query, following `nxt` from zero is a shortest path and `cnt` is its number of edges.

Every answer is appended after applying the current query. The source does not need to traverse the whole path to count its length because `cnt` is maintained incrementally.

## Complexity detail

Creating `nxt` takes $O(n)$ time and space. Each query performs constant work outside the while loop. Whenever the loop iterates, it marks one previously active positive city with sentinel zero. That city can never be removed again. Across all queries, there are at most $n-2$ such successful iterations.

The total time is therefore $O(n+q)$ by amortized analysis, even though one individual query can skip $O(n)$ cities. The average is not assumed; the permanent deletion argument bounds the sum of all loop iterations.

The successor array uses $O(n)$ auxiliary space. The returned answer has $q$ entries; excluding output gives $O(n)$ auxiliary space, while including it gives $O(n+q)$ total storage.

## Alternatives and edge cases

- **Run BFS after every query:** This works as in problem 3243 but costs $O(q(n+q))$, which is too large when both limits are $10^5$.
- **Disjoint-set “next active” structure:** A union-find successor technique can also skip removed indices. The explicit `nxt` links already act as a simple deletion structure under noncrossing intervals and achieve linear amortized time.
- **Maintain all-pairs or all-source distances:** The graph is much too large for quadratic state, and only the zero-to-destination distance is requested.
- **Crossing queries:** The algorithm relies critically on their absence. With roads such as `u1 < u2 < v1 < v2`, marking bypassed endpoints inactive can discard a later useful combination.
- **Nested shortcuts:** A later outer shortcut can remove nodes and inner shortcut endpoints still present on the current path. Following `nxt` jumps over nodes already removed and deletes each remaining active intermediate node once.
- **Disjoint shortcuts:** They modify separate portions of the successor path and their savings accumulate.
- **Query from an inactive `u`:** `nxt[u]` is zero, so the condition fails. Under the noncrossing guarantee, the road cannot improve the maintained shortest path.
- **Current successor equals `v`:** The road duplicates the currently represented step in terms of path progress, so it saves nothing.
- **Current successor exceeds `v`:** The path already jumps farther from `u`; replacing it with a shorter forward jump cannot improve the distance.
- **Direct road from zero to `n - 1`:** All intermediate active cities are removed, `cnt` becomes one, and later answers remain at the theoretical minimum.
- **Tuple assignment:** Reading the old successor and clearing the current link must be logically simultaneous. A two-statement implementation should save the old successor in a temporary variable before writing zero.
- **No destination entry in `nxt`:** The loop stops when `i == v` and never reads `nxt[v]` at that point. Query constraints also ensure every source `u` has a valid array index.

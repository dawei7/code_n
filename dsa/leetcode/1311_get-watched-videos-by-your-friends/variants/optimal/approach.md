## General

People and friendships form an undirected graph. A person's identifier is a vertex, and each friendship is an edge. “Friends at level `k`” means vertices whose shortest-path distance from `id` is exactly `k`, not everyone reachable within `k` steps.

The Optimal solution uses breadth-first search because BFS discovers an unweighted graph one distance layer at a time. After advancing exactly `level` layers, the queue contains precisely the people whose shortest distance is that level. The solution then counts videos watched by those people and sorts video titles by frequency and alphabetical order.

**Starting at distance zero**

`q = deque([id])` places the starting person in the queue. `vis = {id}` immediately marks that person discovered.

At this point, the queue is exactly distance zero. Marking on discovery is important in an undirected friendship graph. Without it, two people in one layer could both enqueue the same friend, and edges back to already processed people could create cycles.

**Advancing one complete friendship level**

The outer loop runs `level` times. Each iteration represents one edge of distance.

Inside it, `range(len(q))` captures the number of people in the current layer before new friends are appended. Each current person is removed, and every identifier in `friends[i]` is examined. An unvisited friend is marked immediately and appended.

Because newly appended people are not processed during the same frozen inner loop, they form the next layer. After the first outer iteration, the queue holds shortest-distance-one friends. After the second, it holds shortest-distance-two people, and so on.

The visited set is what makes the distance exact. Suppose a person is reachable through both a short path and a longer path. BFS discovers and marks that person along the shortest path first. A later longer route cannot enqueue the person into a deeper layer. Thus, the final queue excludes anyone whose true shortest distance is less than `level`.

The graph is undirected according to the contract, but the BFS logic would also find directed shortest distances if `friends` were interpreted as outgoing adjacency lists.

**Why the queue itself is the target layer**

The solution does not copy the queue after the BFS. Once the outer loop has run exactly `level` times, every person from smaller distances has been popped, and people at greater distances have not yet been expanded or even necessarily discovered beyond the current frontier.

Therefore, iterating `for i in q` directly visits exactly the desired people.

If the connected component ends before the requested level, the queue becomes empty. Later outer iterations process zero people, and video counting produces an empty result, which is correct because nobody exists at that exact distance.

**Counting video frequencies**

`cnt = Counter()` maps each title to the number of times it appears across the watched-video lists of people in the target layer.

For every target person `i`, the nested loop visits every `v in watchedVideos[i]` and performs `cnt[v] += 1`. A title watched by two different level friends therefore gets frequency two. If a title appears once among one friend and once among another, both occurrences contribute.

The algorithm counts video-list entries exactly as supplied. The local constraints do not explicitly state that one person's list contains unique titles, so a duplicate title inside one list would also increment more than once. Under the ordinary interpretation, each entry represents a watched video occurrence.

People at other distances contribute nothing because they are no longer in the queue or have not reached it at the chosen layer.

**Sorting by two keys**

`cnt.keys()` contains each distinct title seen in the target layer exactly once. The return expression sorts those keys using

`key=lambda k: (cnt[k], k)`.

Python compares tuples lexicographically. It first compares `cnt[k]`, so lower-frequency titles come first. If frequencies are equal, it compares the title strings `k` alphabetically, so the lexical tie rule is satisfied.

For level-one friends who collectively watched `B` once and `C` twice, the key for `B` is `(1, "B")` and the key for `C` is `(2, "C")`, placing `B` first. If both frequencies were one, alphabetical order would decide.

Only distinct titles appear in the returned list; frequency determines order but is not itself included in the output.

**Why the whole algorithm is correct**

Initially, the queue contains exactly the vertex at distance zero. Assume before some outer iteration it contains exactly the vertices at distance $d$. Expanding all of them finds every vertex reachable in $d+1$ steps. Immediate visited marking removes vertices already discovered at distance at most $d$ and coalesces multiple shortest routes to one person. The remaining appended vertices are exactly those whose shortest distance is $d+1$.

By induction, after `level` expansions, `q` is exactly the requested friend layer. The counter then counts every video entry from exactly those people. Finally, tuple sorting implements increasing frequency and alphabetical tie-breaking. Each stage therefore matches one part of the contract.

## Complexity detail

Let $n$ be the number of people, $E$ the total number of friendship adjacency entries scanned during BFS, $S$ the number of watched-video entries belonging to people in the selected layer, and $V$ the number of distinct titles among those entries.

Each person is marked at most once and processed at most once before or within the required layers. Each processed adjacency entry is examined once, giving $O(n+E)$ BFS time in the broad graph bound. Counting takes $O(S)$ expected time with a hash counter.

Sorting $V$ distinct title keys costs $O(V\log V)$ comparisons. Titles are at most eight characters, so string-comparison length is bounded by a small constant under the constraints. Total time is

$$
O(n+E+S+V\log V).
$$

`vis` and the queue use $O(n)$ space. The counter and distinct-title result use $O(V)$ space. This gives $O(n+V)$ auxiliary and result-related storage, matching the manifest.

## Alternatives and edge cases

- **Depth-first search with stored distances:** DFS can traverse the graph while maintaining best known distances, but BFS obtains unweighted shortest layers directly and more simply.
- **Repeated frontier sets:** Replacing the queue with a set of the next layer can work, but a global visited set is still required to enforce shortest-distance semantics.
- **Count everyone within the level:** That is incorrect. The task asks for shortest path exactly equal to `level`, so smaller layers must be removed before counting.
- **No people at the requested level:** The queue is empty and the sorted key list is empty.
- **Several shortest paths to one person:** Immediate `vis.add(j)` ensures the person appears only once in the layer and their videos are not double-counted.
- **Cycles and friendship back-edges:** The visited set prevents returning to the starting person or looping between friends.
- **Disconnected graph:** Only the starting person's connected component can enter the queue; unreachable people correctly contribute nothing.
- **Same video watched by several target friends:** Every entry increments the shared counter, raising that title's frequency.
- **Frequency tie:** The second tuple component, the title itself, orders tied videos alphabetically.
- **No frequency in output:** `sorted(cnt.keys(), ...)` returns titles only, as required.
- **Level one:** One outer expansion removes `id` and leaves exactly direct friends.
- **Large level beyond component depth:** Empty frontiers remain empty through the remaining fixed iterations and produce an empty answer.
- **Duplicate friendship entries outside the usual graph representation:** Immediate visited marking prevents duplicate person insertion even if an adjacency list repeats an ID.

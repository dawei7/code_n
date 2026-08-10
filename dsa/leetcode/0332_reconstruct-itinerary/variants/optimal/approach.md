## General

**Model tickets as directed edge occurrences.**

Each airport is a vertex, and each ticket `[from, to]` is one directed edge from `from` to `to`. Duplicate tickets are distinct edge occurrences even when their endpoint strings are identical. The required itinerary starts at `JFK`, uses every edge exactly once, and lists the visited vertices in order. In graph terminology, it is a directed Eulerian trail with a fixed starting vertex.

The input guarantee says at least one such trail exists. The remaining tasks are to consume every edge without losing the ability to finish and to choose the lexically smallest valid trail.

**Prepare destinations so removing the smallest is cheap.**

The source creates a dictionary `g` mapping each departure airport to a list of its unused arrival airports. It iterates through `sorted(tickets, reverse=True)`, which sorts ticket pairs in descending lexicographic order. Because pair comparison examines the departure first and destination second, all destinations stored under one departure are appended in descending order.

For example, outgoing destinations `ATL`, `LAX`, and `SFO` are stored as `[SFO, LAX, ATL]`. Calling `pop()` removes the last element, `ATL`, in constant time. Thus every recursive choice consumes the currently smallest lexical destination without the cost of deleting from the front of a list.

Using a list rather than a set is essential. If two identical tickets exist, both destination entries are appended and both must be popped on separate traversals.

The `defaultdict(list)` also gives an unseen arrival airport an empty outgoing list. Testing `while g[f]` at a dead end therefore works without a separate key check.

**Why ordinary forward greediness is unsafe.**

It is tempting to build the returned itinerary from left to right by always taking the smallest unused destination. That can enter a dead end before all tickets have been used. Consider tickets `JFK -> KUL`, `JFK -> NRT`, and `NRT -> JFK`. The smallest immediate destination is `KUL`, but placing it second would strand the route. The only complete itinerary is `JFK, NRT, JFK, KUL`.

The exact source still explores the smallest edge first, but it does not immediately commit visited airports to the front of the answer. It uses Hierholzer's postorder construction: an airport is appended only after every outgoing ticket reachable from that call has been exhausted. The route is built backward, so a dead-end excursion naturally becomes the end of the final itinerary rather than incorrectly becoming its beginning.

**Meaning of the recursive traversal.**

Calling `dfs(f)` consumes all still-unused outgoing edges that the call encounters from airport `f`. While `g[f]` is nonempty, it removes the smallest destination `t` and recursively calls `dfs(t)`. Popping the edge before recursion marks that specific ticket occurrence as used.

Only when `f` has no unused outgoing ticket does the call execute `ans.append(f)`. This is postorder: destinations that become dead ends are appended before the airports that led to them. The list `ans` is consequently the itinerary in reverse.

After `dfs('JFK')` returns, `ans[::-1]` reverses that postorder list into forward travel order.

**Walk through the second example.**

For the tickets

`JFK -> SFO`, `JFK -> ATL`, `SFO -> ATL`, `ATL -> JFK`, and `ATL -> SFO`,

the smallest outgoing edge from `JFK` is `ATL`. The recursive consumption chain is

$$
\text{JFK}\to\text{ATL}\to\text{JFK}\to\text{SFO}
\to\text{ATL}\to\text{SFO}.
$$

The final `SFO` has no unused outgoing edge and is appended first. As calls finish, airports are appended in the reverse sequence

$$
[\text{SFO},\text{ATL},\text{SFO},\text{JFK},\text{ATL},\text{JFK}].
$$

Reversing gives

$$
[\text{JFK},\text{ATL},\text{JFK},\text{SFO},\text{ATL},\text{SFO}],
$$

the required lexically smallest itinerary.

The dead-end example shows the more subtle behavior. DFS first consumes `JFK -> KUL`, immediately appends `KUL`, then returns to the still-active `JFK` call and consumes `JFK -> NRT -> JFK`. Postorder reversal places the `KUL` excursion last, yielding the only complete route. This is how Hierholzer's method repairs a locally premature edge without restoring or searching over tickets.

**Why every ticket is used exactly once.**

Each ticket occurrence appears once in one adjacency list. The only way to traverse an edge is to remove its destination with `pop()`. A removed entry cannot be removed again, so no ticket is reused. The `while` loop continues until every outgoing list reached by traversal is empty.

Under the guarantee that all tickets form a valid itinerary starting at `JFK`, every edge belongs to the Eulerian structure reachable from that start. The traversal therefore consumes all $E$ tickets. It appends one airport for the initial start plus one for each consumed edge, so the reversed result has exactly $E+1$ airports.

**Why postorder reversal forms a continuous itinerary.**

When a call at `f` follows an edge to `t`, the recursive call completely resolves the trail segment beginning at `t` before `f` is appended. In reverse postorder, `f` therefore appears immediately before the already resolved segment at the correct splice point.

One can view the process as finding trails until they reach dead ends and splicing additional cycles or branches at vertices that still have unused outgoing edges. Hierholzer's theorem guarantees that, when an Eulerian trail exists, exhausting edges this way and reversing the finish order produces a single trail using them all. The stack of recursive calls provides the splice positions automatically.

**Why lexical ordering is minimal.**

Whenever the traversal has a choice of unused outgoing tickets from one airport, `pop()` selects the smallest destination. If that choice can appear next in the final unresolved portion, it is lexically best at the first position where alternatives differ. If it leads to a dead end too early, postorder delays that completed excursion until the point where it can legally finish, while the active call continues with the next outgoing edge.

This is the lexical version of Hierholzer traversal: edges are exhausted in ascending destination order, and completed segments are inserted through reverse finish order. Consider another valid itinerary and its first airport position that differs from the produced result. Up to that position both have consumed the same prefix structure. The algorithm used the smallest available outgoing destination that can occupy that position after necessary dead-end segments are spliced; the alternative uses a larger one. Therefore the alternative cannot be lexically smaller.

No exponential backtracking is required. The existence guarantee plus Eulerian postorder handles feasibility, while sorted adjacency handles the tie-breaking objective.

## Complexity detail

Let $E$ be the number of tickets. Sorting all ticket pairs costs $O(E\log E)$ time. Building the graph is $O(E)$. Every ticket is popped and traversed once, every airport occurrence is appended once, and reversing the result is $O(E)$. Total time complexity is $O(E\log E)$.

The adjacency lists store $E$ destination entries, `ans` stores $E+1$ airports, and recursive calls can reach depth $E+1$. Total auxiliary space is $O(E)$.

The manifest gives the same asymptotic bounds but describes an iterative Hierholzer traversal. The exact optimal source is recursive; its call stack is part of the $O(E)$ space. With at most `300` tickets, that recursion depth remains modest.

## Alternatives and edge cases

- **Iterative Hierholzer traversal:** Maintain an explicit airport stack, push the smallest unused destination while possible, and move dead ends into the result. This has the same $O(E\log E)$ preprocessing and $O(E)$ space, avoids recursion, and matches the manifest wording.

- **Min-heaps per departure:** Push destinations into a heap and pop the smallest during traversal. This avoids globally sorting tickets but makes edge removal $O(\log d)$ for outdegree $d$; the total remains $O(E\log E)$.

- **Backtracking over tickets:** Try destinations in sorted order and undo choices that cannot finish. It is conceptually direct but may explore exponentially many partial routes. Hierholzer uses the Eulerian structure to avoid that search.

- **Duplicate tickets:** Adjacency lists preserve duplicate destination strings as separate entries, so each identical ticket occurrence is consumed once.

- **A forced dead end:** Postorder deliberately appends that airport early to the reverse result, placing it late in the final itinerary where it belongs.

- **One ticket:** DFS consumes the sole edge, appends its destination, then appends `JFK`; reversal returns the two-airport route.

- **Airports with no outgoing tickets:** Accessing `g[f]` produces an empty list, the loop skips, and the airport is appended as the current trail endpoint.

- **Fixed start:** Traversal must begin with `dfs('JFK')`; choosing a graph vertex merely because it has outgoing edges would violate the contract even if another Euler trail existed.

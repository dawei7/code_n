## General

The competitive solution builds a shortest-path DAG with bidirectional breadth-first search. One frontier starts at `beginWord`, the other at `endWord`, and each iteration expands the smaller frontier.

Because the active search direction can swap, every stored edge is deliberately oriented so `tree[word]` contains predecessors on a route back toward `beginWord`. A final recursive comprehension reconstructs forward paths.

**Dictionary preparation**

`words = set(wordList)` provides efficient membership and removal. If `endWord` is absent, the method returns `[]` because the final sequence word must be allowed.

The two frontier sets start as `{beginWord}` and `{endWord}`. `is_reversed` is false while expansion moves from the beginning side and true while expansion moves from the end side.

`tree` is a `defaultdict(set)`. Sets retain multiple parents without duplicate edges generated through repeated mutation routes.

**Why expand the smaller side**

A word may have many neighbors. Ordinary BFS can grow roughly by a branch factor at each depth. Searching from both ends and expanding the smaller current frontier often reduces the number of vertices generated before the searches meet.

After producing `new_left`, the source compares its size with the opposite `right` frontier. If it is larger, it swaps the frontier roles and flips `is_reversed`.

The optimization changes traversal direction but not graph meaning because edge orientation is adjusted with the flag.

**Removing the expanded layer**

At the start of an iteration, `words -= left` removes every current-frontier word from the undiscovered pool.

This prevents mutations from pointing back into an already processed layer and prevents cycles. Words in a newly generated frontier remain available for the entire current expansion, allowing multiple same-depth parents to connect to them.

On a later expansion, that frontier itself is removed. Hence stored edges always cross BFS layers rather than returning to older ones.

**Generating neighbors**

For each frontier word, a generator replaces every position with every lowercase letter. Candidate construction uses two slices and one inserted character.

Candidates absent from `words` are skipped. This discards nonexistent dictionary words and previously removed layers.

The original character is also generated, but the current word has just been removed from `words`, so it cannot become a self-edge.

**Detecting the meeting layer**

If `new_word in right`, the two searches have connected. `is_found` becomes true and the meeting edge is stored.

The source does not break immediately. It finishes the complete current frontier, preserving every meeting edge at the same shortest combined depth. Only after the level finishes does the outer loop stop.

Neighbors that do not meet the opposite frontier are added to `new_left`. On a meeting iteration, some extra dead-end edges may also be stored because the code does not suppress nonmeeting candidates after `is_found` becomes true. They cannot create invalid returned paths: backtracking outputs only branches that eventually reach `beginWord`, but they can add avoidable search work.

**Keeping edges oriented for reconstruction**

When expanding from the begin side, `word` is closer to `beginWord` and `new_word` is farther away. The source stores `tree[new_word].add(word)`, making `word` a predecessor.

When expanding from the end side, traversal moves in the opposite physical direction. Here `new_word` is closer to `beginWord` than current `word`, so the source stores `tree[word].add(new_word)`.

In both cases, following `tree[current]` moves toward `beginWord`. That consistent orientation is the central correctness condition of bidirectional DAG construction.

**Backtracking behavior**

`backtracking(tree, beginWord, word)` returns every path from `beginWord` through the predecessor DAG to `word`.

If `word == beginWord`, it returns `[[beginWord]]`. Otherwise, for each predecessor `new_word`, it recursively obtains all paths ending there and appends the current `word` to each.

Starting at `endWord` therefore produces complete forward sequences. If the search never connects, `tree[endWord]` has no productive predecessor chain and the comprehension returns an empty list.

**Why shortestness is preserved**

Each frontier represents one BFS distance from its respective endpoint. The first layer where an edge meets the opposite frontier gives the minimum combined distance.

Finishing that layer captures all connections of the same combined length. Stopping before another expansion prevents longer meeting routes from entering the productive DAG.

Removing expanded layers makes the graph acyclic by BFS depth. Direction correction ensures backtracking always moves toward the beginning, so every successful returned route follows one edge per shortest layer.

**Example structure**

From `hit`, one side reaches `hot`, then `dot` and `lot`. From `cog`, the other side can reach `dog` and `log`.

Meeting edges connect `dot` with `dog` and `lot` with `log` at the same combined depth. Regardless of which frontier was smaller and expanded, orientation makes `tree[cog]`-side recursion eventually reach `hit`.

The result contains both shortest sequences. Set iteration may reverse their presentation order, which is allowed.

**Active versus alternative implementation**

The file also defines unidirectional `Solution2`, but the selected entry point is the first `Solution`.

The active source imports `defaultdict` and `ascii_lowercase` correctly. It does not require `deque` because frontiers are sets.

## Complexity detail

Let $W$ be dictionary size, $L$ word length, $E$ stored DAG edges, and $R$ total word references in returned sequences.

In the worst case, bidirectional search may still expand $O(W)$ words. Each tries $26L$ candidates, and Python slicing, concatenation, and hashing cost $O(L)$ per candidate, giving $O(WL^2)$ worst-case construction time. Backtracking costs at least $O(R)$ and may also traverse dead branches stored on the meeting layer. A precise bound is $O(WL^2+E+R+D)$, where $D$ is dead-branch reconstruction work.

The remaining-word set and two frontiers use $O(W)$ references. The DAG uses $O(W+E)`, recursion/path construction uses depth $O(W)$ in the loosest bound, and returned lists use $O(R)`. Peak space including output is $O(W+E+R)`.

Bidirectional expansion often gives a major practical reduction, approximately exploring toward half the solution depth from each side, but its worst-case asymptotic word bound remains linear in all reachable dictionary vertices.

The manifest's generic $O(N+R)$ is meaningful only if $N$ includes generated graph work and edges. It is not simply the count of input words under Python string-construction costs.

## Alternatives and edge cases

- **Level-synchronous unidirectional BFS:** Easier to reason about and can preserve all same-depth predecessors with a distance map.
- **Wildcard buckets:** Precompute pattern-to-word groups to avoid generating all alphabet substitutions repeatedly.
- **Queue complete paths:** Avoids a separate backtracking phase but duplicates prefixes and can explode in memory.
- **Expand the larger frontier:** Correct if otherwise unchanged, but forfeits the main bidirectional performance benefit.
- **Forget `is_reversed`:** Produces inconsistent edge directions and breaks reconstruction.
- **Stop on the first meeting edge:** Misses other shortest sequences meeting elsewhere in the same layer.
- **End word absent:** Immediate empty output.
- **Begin word present in the dictionary:** It is removed when its frontier is expanded, preventing a back edge.
- **Sparse disconnected graph:** Search eventually empties a frontier, and backtracking returns no path.
- **Multiple parents:** `defaultdict(set)` retains them while deduplicating edges.
- **Set output order:** Nondeterministic but permitted.
- **Generated original word:** It has been removed from `words`, so no self-loop is stored.
- **Extra meeting-layer branches:** They may be explored as dead ends but cannot reach the base case and therefore cannot produce invalid sequences.
- **Recursive output size:** The constraint caps total shortest-sequence material, but reconstruction is necessarily output-sensitive.
- **Active imports:** `defaultdict` and `ascii_lowercase` are present; the alternative `Solution2` is inert.
